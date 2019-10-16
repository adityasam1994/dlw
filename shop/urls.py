from django.urls import path
from . import views

app_name="shop"

urlpatterns=[
    path('', views.home, name="home"),
    path('product_detail/<pid>/<sl>/', views.product_detail, name="product_detail"),
    path('loginnow/',views.loginnow, name="loginnow"),
    path('mycart/', views.mycart, name="mycart"),
    path('myorder/', views.myorder, name="myorder"),
    path('checkout/', views.checkout, name="checkout"),
    path('add_to_cart/<pid>/<sl>/', views.add_to_cart, name="add_to_cart"),
    path('removefromcart/<pid>/<sl>/',views.removefromcart, name="removefromcart"),
    path('updatecart/<clen>',views.updatecart, name="updatecart"),
    path('removefromcart/<pid>/',views.removefromcart, name="removefromcart"),
    path('removefromorder/<pid>/<oid>/',views.removefromorder, name="removefromorder"),
    path('removefromcartdirect/<pid>/',views.removefromcartdirect, name="removefromcartdirect"),
    path('add_to_cart_direct/<pid>', views.add_to_cart_direct, name="add_to_cart_direct"),
    path('logoutnow/', views.logoutnow, name="logoutnow"),
    path('signupnow/', views.signupnow, name="signupnow"),
    path('userdetail/', views.userdetail, name="userdetail"),
    path('add_address/', views.add_address, name="add_address"),
    path('edit_address/<aid>/', views.edit_address, name="edit_address"),
    path('del_address/<aid>/', views.del_address, name="del_address"),
    path('place_order/<aid>/', views.place_order, name="place_order"),
    path('offers/', views.offers, name="offers"),
]