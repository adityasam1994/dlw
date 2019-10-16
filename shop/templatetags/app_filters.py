from django import template
from django.template.defaultfilters import stringfilter
import datetime
from django.utils import timezone

register = template.Library()

@register.filter(name='getimage')
@stringfilter
def getimage(string):
    from shop.models import Image
    im = Image.objects.filter(product_id=int(string))
    return im[0]

@register.filter(name='getallimages')
@stringfilter
def getallimages(string):
    from shop.models import Image
    im = Image.objects.filter(product_id=int(string))
    return im

@register.filter(name="getreviews")
@stringfilter
def getreviews(string):
    from shop.models import Review
    re = Review.objects.filter(product_id=int(string))
    return re

@register.filter(name="getcustomer")
@stringfilter
def getcustomer(string):
    from django.contrib.auth.models import User
    u = User.objects.get(id=int(string))
    return u

@register.filter(name='times') 
def times(number):
    num=0
    if(number <=5 ):
        num=number
    else:
        num=5
    return range(num)

@register.filter(name="get_average_stars")
def get_average_stars(number):
    from shop.models import Review
    re = Review.objects.filter(product_id=number)
    if len(re) != 0:
        total=0
        for r in re:
            total=total+r.rating

        average=total/len(re)
        return int(round(average))
    else:
        return 0

@register.filter(name="get_star_count")
def get_star_count(number):
    from shop.models import Review
    re = Review.objects.filter(product_id=number)
    return len(re)

@register.filter(name="checkcart")
def checkcart(number, uid):
    from shop.models import Customer
    from shop.models import Product
    product=Product.objects.get(id=number)
    mycart = Customer.objects.get(id=uid).cart
        
    if mycart != "" and mycart is not None:
        pp=1
        cartsplit = mycart.split(",")
        for c in cartsplit:
            cc= c.split("/")
            if int(cc[0]) == number:
                pp=int(cc[1])
        return pp
    else:
        return 1    

@register.filter(name="checkcartbtn")
def checkcartbtn(number, uid):
    from shop.models import Customer
    from shop.models import Product
    product=Product.objects.get(id=number)
    mycart = Customer.objects.get(customer_id=uid).cart

    if mycart != "" and mycart is not None:
        pp=1
        cartsplit = mycart.split(",")
        for c in cartsplit:
            cc= c.split("/")
            if int(cc[0]) == number:
                pp=int(cc[1])
                return True
    else:
        return False

@register.filter(name="get_item_name")
@stringfilter
def get_item_name(string):
    from shop.models import Product
    sp=string.split("/")
    pro=Product.objects.get(id=int(sp[0])).name
    return pro

@register.filter(name="get_item_price")
@stringfilter
def get_item_price(string):
    from shop.models import Product
    from shop.models import Offer
    per=0
    sp=string.split("/")
    off = Offer.objects.filter(percent_discount=True)
    for o in off:
        pros = o.product.all()
        for pro in pros:
            if pro.id == int(sp[0]):
                per = o.percent
    pro=Product.objects.get(id=int(sp[0])).price
    prod = pro - (pro*per/100) 
    return prod

@register.filter(name="get_item_qty")
@stringfilter
def get_item_qty(string):
    from shop.models import Product
    sp=string.split("/")
    return sp[1]

@register.filter(name="get_total_price")
@stringfilter
def get_total_price(string):
    from shop.models import Product
    sp=string.split("/")
    pr = Product.objects.get(id=int(sp[0])).price
    total=pr*int(sp[1])
    return total

@register.filter(name="get_item_image")
@stringfilter
def get_item_image(string):
    from shop.models import Image
    sp=string.split("/")
    pr = Image.objects.filter(product_id=int(sp[0]))

    return pr[0]

@register.filter(name="get_cart_total")
def get_cart_total(list):
    from shop.models import Product
    from shop.models import Offer
    tot=0
    for s in list:
        per=0
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
    return tot

@register.filter(name="get_pid")
@stringfilter
def get_pid(string):
    sp=string.split("/")
    return int(sp[0])

@register.filter(name="splitorder")
def splitorder(number):
    from shop.models import Order
    orde = Order.objects.get(id=number).product_id
    sp=orde.split(",")
    return sp

@register.filter(name="checkoffer")
def checkoffer(number):
    from shop.models import Offer
    off = Offer.objects.filter(percent_discount=True)
    ooo = None
    for o in off:
        pros = o.product.all()
        for p in pros:
            if p.id==number:
                ooo= o.id
    return ooo

@register.filter(name="get_off_price")
def get_off_price(number,oid):
    from shop.models import Offer
    off = Offer.objects.get(id=oid)
    dis = off.percent
    newprice = int(number * (100-dis)/100)
    return newprice

@register.filter(name="get_off_percent")
def get_off_percent(number):
    from shop.models import Offer
    off = Offer.objects.get(id=number)
    dis = int(off.percent)
    return dis

@register.filter(name="get_item_count")
def get_item_count(number):
    from shop.models import Customer
    cus = Customer.objects.get(customer_id = number)
    cart = cus.cart
    cartsplit = cart.split(",")
    return len(cartsplit)

@register.filter(name="get_total")
def get_total(number):
    from shop.models import Customer
    from shop.models import Product
    cus = Customer.objects.get(customer_id = number)
    cart = cus.cart
    cartsplit = cart.split(",")
    tot=0
    for c in cartsplit:
        cc=c.split("/")
        price = Product.objects.get(id=int(cc[0])).price
        tot = tot + price*int(cc[1])
    return tot

@register.filter(name="canceldate")
def canceldate(number):
    from shop.models import Shop_detail
    cp = Shop_detail.objects.get(id=1).cancellation_period
    number += datetime.timedelta(days=cp)
    if timezone.now() > number:
        return True
    else:
        return False
    
    