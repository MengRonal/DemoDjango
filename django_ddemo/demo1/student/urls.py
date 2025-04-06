from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path (route='home/' , view=views.home , name="home"),
    path (route='about/' , view=views.about , name="about"),
    path (route='contact/' , view=views.contact , name="contact"),
    path (route= "product/" ,view=views.product , name="product"),
    path(route = 'category/' , view=views.category , name='category'),
    path(route='staff/' , view=views.staff , name= 'staff'),
    path(route="detail/<int:id>" ,view=views.detail, name="detail"),
    path(route="ProductList/" , view=views.Product_list ,name="ProductList")

]