from django.shortcuts import render, HttpResponse, reverse, redirect, HttpResponseRedirect
from .models import Customer,Product, Offer, Category, Image, Address, Order, Review, Shop_detail
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.models import User
import re 
from datetime import date 
from django.db.models import Q

# Create your views here.

def home(request):
    if request.method == "POST":
        query=request.POST.get("query")
        if query:
            pros=Product.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(Category__name__icontains=query)
                ).distinct()

            return render(request, 'products/query.html',{'products':pros, 'query':query})
        else:
            return HttpResponseRedirect(reverse('shop:home'))
    else:
        pros = Product.objects.filter(available=True).order_by('created_at')
        products=create_card_products(pros)

        bestpro = Product.objects.filter(available=True).order_by("sold")

        bp=[]
        if(len(bestpro) >= 9):
            for i in range(8):
                bp.append(bestpro[i])
        else:
            bp=bestpro

        bestproducts = create_card_products(bp)
        context={
            'products':products,
            'products_small':pros,
            'bestproducts':bestproducts,
        }
        return render(request, 'products/home.html',context)

def create_card_products(products):
    pro=[]
    pro0=[]
    count=0
    for p in products:
        count = count+1
        if(count == 3):
            pro0.append(p)
            pro.append(pro0)
            pro0=[]
            count=0
        pro0.append(p)

    rem = len(products)%3
    di = len(products)/3
    pp=[]
    if rem >=1:
        pp.append(products[int(di)+2])
        if rem ==2:
            pp.append(products[int(di)+3])
    
    if pp != []:
        pro.append(pp)
    return pro

def product_detail(request,pid,sl):
    if request.method == "POST":
        re = request.POST.get("review")
        rat=request.POST.get("stars")
        if re !="":
            rev = Review()
            rev.customer_id= request.user.id
            rev.product_id = pid
            rev.review = re
            rev.rating=rat
            rev.save()
        return HttpResponseRedirect(reverse('shop:product_detail', args=(pid,sl, )))
    else:
        product=Product.objects.get(id=pid)
        return render(request, 'products/details.html',{"product":product})

def findage():
    today = date.today()
    birthDate = Customer.objects.get(id=1).dob
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 

def add_to_cart(request,pid,sl):
    if request.method == "POST":
        pid = request.POST.get("proid")
        itemcount = request.POST.get("itemcount")
        u = Customer.objects.get(id=request.user.id)
        mycart=u.cart
        if mycart=="":
            mycart=pid+"/"+itemcount
        else:
            newcart=[]
            cartsplit = mycart.split(",")
            test=0
            for c in cartsplit:
                cc= c.split("/")
                if cc[0] == pid:
                    test=test+1
                    newcart.append(pid+"/"+itemcount)
                else:
                    newcart.append(c)
            
            mycart = ",".join(newcart)
            if test==0:
                mycart=mycart+","+pid+"/"+itemcount
                
        u.cart=mycart
        u.save()
        return HttpResponseRedirect(reverse('shop:product_detail', args=(pid,sl, )))
    else:
        return HttpResponseRedirect(reverse('shop:product_detail', args=(pid,sl, )))

def add_to_cart_direct(request, pid):
    cust=Customer.objects.get(id=request.user.id)
    mycart=cust.cart
    if mycart != "":
        mycart= mycart+","+pid+"/1"
    else:
        mycart = pid+"/1"
    cust.cart=mycart
    cust.save()
    return HttpResponseRedirect(reverse('shop:home'))

def removefromcart(request, pid, sl):
    cust=Customer.objects.get(id=request.user.id)
    car=cust.cart
    cartsplit=car.split(",")
    
    newcart=[]
    for c in cartsplit:
        cc = c.split("/")
        if cc[0] != pid:
            newcart.append(c)
    n=",".join(newcart)

    cust.cart=n
    cust.save()
    return HttpResponseRedirect(reverse('shop:product_detail', args=(pid,sl, )))

def loginnow(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password is not None:
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("shop:home")
            else:
                messages.error(request,"Username or Password is wrong, Please try again!")
                return redirect("shop:loginnow")
        else:
            messages.error(request,"All fields are required")
            return redirect("shop:loginnow")
    else:
        return render(request, 'products/login.html')

def signupnow(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        
        if username is not None and email is not None and password is not None and password2 is not None and first_name is not None and last_name is not None:
            if password != password2:
                messages.error(request,"Passwords doesn't match")
                return redirect("shop:signupnow")
            else:
                uu = User.objects.filter(username = username)
                if uu is None:
                    user = User.objects.create_user(username = username,email = email,
                    first_name= first_name,last_name = last_name,password = password)
                    
                    auth_login(request, user)
                    newc = Customer()
                    newc.customer_id = request.user.id
                    newc.save()
                    return redirect("shop:home")
                else:
                    messages.error(request,"Username already exists")
                    return redirect("shop:signupnow")
    else:
        return render(request,'products/signup.html')


def emailvalid(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):  
        return True
          
    else:  
        return False

def logoutnow(request):
    logout(request)
    return redirect("shop:home")

def mycart(request):
    cust = Customer.objects.get(id=request.user.id)
    mycart=[]
    if cust.cart != "":
        mycart=cust.cart.split(",")
    return render(request, 'products/mycart.html', {'cart':mycart})

def myorder(request):
    orders = Order.objects.filter(customer_id=request.user.id).order_by('order_date')
    print(len(orders))
    return render(request, 'products/myorders.html', {'orders':orders})

def updatecart(request, clen):
    if request.method == "POST":
        mycart=""
        for i in range(int(clen)):
            pid = request.POST.get("pid"+str(i+1))
            qty = request.POST.get("qty"+str(i+1))
            if mycart == "":
                mycart = pid+"/"+qty
            else:
                mycart = mycart+","+pid+"/"+qty

        cust=Customer.objects.get(id=request.user.id)
        cust.cart = mycart
        cust.save()
        return HttpResponseRedirect(reverse('shop:mycart'))

def removefromcart(request, pid):
    cust=Customer.objects.get(id=request.user.id)
    mycart=cust.cart
    sp=mycart.split(",")

    newcart=""
    for s in sp:
        spp=s.split("/")
        if spp[0] != pid:
            if newcart == "":
                newcart = s
            else:
                newcart = newcart+","+s
    cust.cart = newcart
    cust.save()
    return HttpResponseRedirect(reverse('shop:mycart'))

def removefromorder(request, pid, oid):
    cust=Order.objects.get(id=oid)
    mycart=cust.product_id
    sp=mycart.split(",")
    newcart=""
    for s in sp:
        print(s)
        spp=s.split("/")
        if spp[0] != pid:
            if newcart == "":
                newcart = s
            else:
                newcart = newcart+","+s
    if newcart == "":
        cust.delete()
    else:
        cust.product_id = newcart
        cust.save()
    return HttpResponseRedirect(reverse('shop:myorder'))

def removefromcartdirect(request, pid):
    cust=Customer.objects.get(id=request.user.id)
    mycart=cust.cart
    sp=mycart.split(",")

    newcart=""
    for s in sp:
        spp=s.split("/")
        if spp[0] != pid:
            if newcart == "":
                newcart = s
            else:
                newcart = newcart+","+s
    cust.cart = newcart
    cust.save()
    return HttpResponseRedirect(reverse('shop:home'))

def checkout(request):
    if request.method == "POST":
        addid = request.POST.get("address_id")
        check = request.POST.get("checks")
        if check == "on":
            return render(request, 'products/payment.html', {"address_id": addid})
        else:
            return HttpResponseRedirect(reverse('shop:mycart'))
    else:
        return HttpResponseRedirect(reverse('shop:mycart'))

def userdetail(request):
    return render(request, "products/userdetail.html")

def add_address(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address=request.POST.get("address")
        phone = request.POST.get("phone")
        if name != "" and address != "" and phone != "":
            add=Address()
            add.customer_id = request.user.id
            add.name = name
            add.address = address
            add.phone = phone
            add.save()
            return HttpResponseRedirect(reverse('shop:mycart'))
        else:
            return HttpResponseRedirect(reverse('shop:mycart'))
    else:
        return HttpResponseRedirect(reverse('shop:mycart'))

def del_address(request, aid):
    add = Address.objects.get(id=aid)
    add.delete()
    return HttpResponseRedirect(reverse('shop:mycart'))

def edit_address(request, aid):
    if request.method == "POST":
        name = request.POST.get("name")
        address=request.POST.get("address")
        phone = request.POST.get("phone")
        if name != "" and address != "" and phone != "":
            add=Address.objects.get(id=aid)
            add.customer_id = request.user.id
            add.name = name
            add.address = address
            add.phone = phone
            add.save()
            return HttpResponseRedirect(reverse('shop:mycart'))
        else:
            return HttpResponseRedirect(reverse('shop:mycart'))
    else:
        return HttpResponseRedirect(reverse('shop:mycart'))
        
def place_order(request, aid):
    cust = Customer.objects.get(customer_id = request.user.id)
    cart = cust.cart
    address = Address.objects.get(id=aid).address
    phone =  Address.objects.get(id=aid).phone
    tot=Shop_detail.objects.get(id=1).delivery_charge
    sp = cart.split(",")
    for s in sp:
        spp = s.split("/")
        off = Offer.objects.filter(percent_discount=True)
        for o in off:
            pros = o.product.all()
            for pro in pros:
                if pro.id == int(spp[0]):
                    per = o.percent
        prd = Product.objects.get(id=int(spp[0])).price
        pr = prd - (prd*per/100)  
        tot=tot+(pr*int(spp[1]))
    
    order = Order()
    order.product_id = cart
    order.customer_id = request.user.id
    order.price = tot
    order.address = address
    order.phone = phone
    order.status = "pending"
    order.payment_mode = "COD"
    order.payment_status = "pending"
    order.save()

    cust.cart = ""
    cust.save()
    return render(request, 'products/ordersuccesspage.html')

def offers(request):
        name=request.POST.get("name")
