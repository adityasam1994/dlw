from django.db import models
from django.urls import reverse
# Create your models here.
class Customer(models.Model):
    customer_id = models.PositiveIntegerField(default=None)
    dob = models.DateField(default=None, null=True, blank=True)
    cart=models.TextField(default=None, null=True, blank=True)

    class Meta:
        ordering = ("customer_id",)

class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(max_length=150, unique=True, db_index=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_by_category',args=[self.slug])

class Product(models.Model):
    Category=models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,default=None,null=True,blank=True)
    name=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100, db_index=True)
    description=models.TextField(blank=True)
    price=models.PositiveIntegerField(default=None)
    available=models.BooleanField(default=True)
    stock=models.PositiveIntegerField()
    sold=models.PositiveIntegerField(default=None,null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

class Image(models.Model):
    product_id = models.PositiveIntegerField(default=None)
    image=models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    
    class Meta:
        ordering=('product_id',)

    def get_absolute_url(self):
        return reverse('shop:image_detail', args=[self.id])


class Order(models.Model):
    product_id = models.CharField(max_length=100)
    customer_id = models.PositiveIntegerField(default=None)
    price = models.PositiveIntegerField(default=None)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100, default=None)
    payment_status = models.CharField(max_length=100, default=None)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("order_date",)

    def __str__(self):
        return self.product_id

    def get_absolute_url(self):
        return reverse('shop:order_detail', args=[self.id])

class Address(models.Model):
    customer_id = models.PositiveIntegerField(default=None)
    name = models.CharField(max_length=100,default=None)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:address_detail", args=[self.id])

class Offer(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug=models.SlugField(max_length=100, db_index=True)
    description=models.TextField(blank=True)
    free_delivery = models.BooleanField(default=False)
    percent_discount = models.BooleanField(default=False)
    quantity_discount = models.BooleanField(default=False)
    include_all = models.BooleanField(default=False)
    include_category = models.BooleanField(default=False)
    category = models.ManyToManyField(Category,default=None,null=True, blank=True)
    include_product = models.BooleanField(default=False)
    product = models.ManyToManyField(Product,default=None,null=True, blank=True)
    percent = models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0)
    quantity = models.PositiveIntegerField(default=None, null = True, blank=True)

    class Meta:
        ordering = ("name",)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:offer_detail", args=[self.id, self.slug])

class Banner(models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to='banners/%Y/%m/%d', blank=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:banner_detail", args=[self.id])

class Review(models.Model):
    customer_id=models.PositiveIntegerField(default=None)
    product_id=models.PositiveIntegerField(default=None,null=True, blank=True)
    review=models.TextField(default=None)
    date=models.DateTimeField(auto_now_add=True)
    rating=models.PositiveIntegerField(default=None)

    class Meta:
        ordering = ("date",)

class Shop_detail(models.Model):
    delivery_charge=models.PositiveIntegerField(default=0)
    cancellation_period=models.PositiveIntegerField(default=1)
    shop_name=models.CharField(max_length=100, default=None, null=True, blank=True)
