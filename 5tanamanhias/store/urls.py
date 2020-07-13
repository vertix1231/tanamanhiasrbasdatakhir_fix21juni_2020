from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.store,name='store'),
    url(r'^carts/$',views.cart,name='cart'),
    url(r'^carts/checkout$',views.checkout,name='checkout'),
    
    
]
