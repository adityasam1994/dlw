from django.contrib import admin
from .models import Customer,Product, Offer, Category, Image, Address, Order, Banner, Review, Shop_detail
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_id','dob']

admin.site.register(Customer,CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available']
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display=['product_id']

admin.site.register(Image, ImageAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['customer_id','status','order_date']

admin.site.register(Order, OrderAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=['customer_id','phone']

admin.site.register(Address, AddressAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display=['name','free_delivery','percent_discount', 'quantity_discount','description']
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Offer, OfferAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display=['name','active']
    list_editable=['active']

admin.site.register(Banner, BannerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=['customer_id', 'date', 'rating']

admin.site.register(Review, ReviewAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display=['delivery_charge', 'cancellation_period', 'shop_name']

admin.site.register(Shop_detail, ShopAdmin)