from .models import Banner, Product, Offer, Address, Order, Shop_detail,Customer

def banner_processor(request):
    ban = Banner.objects.filter(active=True)
    return{'banners':ban}

def myaddresses(request):
    if request.user.is_authenticated:
        add = Address.objects.filter(customer_id = request.user.id)
        return{'addresses':add}
    else:
        return{'addresses':""}

def all_offersPercent(request):
    off = Offer.objects.filter(percent_discount=True)
    return{'offers':off}

def order_total(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(customer_id=request.user.id, status = "pending")
        tot=0
        for order in orders:
            tot=tot+order.price
        return{'order_total':tot}
    else:
        return{'order_total':0}

def delivery_c(request):
    sh = Shop_detail.objects.get(id=1)
    deli = sh.delivery_charge
    return{'delivery_charge':deli}

def cart_total(request):
    if request.user.is_authenticated:
        cus = Customer.objects.get(customer_id = request.user.id)
        cart = cus.cart
        cartsplit = cart.split(",")
        tot=0
        if cart != "":
            for c in cartsplit:
                cc=c.split("/")
                per=0
                off = Offer.objects.filter(percent_discount=True)
                for o in off:
                    pros = o.product.all()
                    for pro in pros:
                        if pro.id == int(cc[0]):
                            per = o.percent
                priced = Product.objects.get(id=int(cc[0])).price
                price = priced - (priced*per/100)
                tot = tot + price*int(cc[1])
            return{'cart_total':tot}
        else:
            return{'cart_total':0}    
    else:
        return{'cart_total':0}

def shopname(request):
    sn = Shop_detail.objects.get(id=1).shop_name
    return{'shop_name':sn}