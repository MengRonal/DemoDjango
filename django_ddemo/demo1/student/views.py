from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Category , Staff ,ProductList
# Create your views here.

def index(request):
    return render(request=request , template_name="index.html")

def home(request):
    return render(request=request,template_name='home.html')

def about (request):
    return  render(request=request,template_name='about.html')

def contact (request):
    return  render(request=request, template_name='contact.html')

def product(request):
    pro = Product.objects.all()
    return render(request=request , template_name='product.html', context={"pro_list":pro} )

def category(request):
    cate = Category.objects.all()
    return render(request=request , template_name='category.html' ,context={'category_list':cate})

def staff(request):
    st = Staff.objects.all()
    return render(request=request , template_name='staff.html' , context={'staff_list':st})
def detail(request , id):
    dt = Staff.objects.get(id=id)
    return render(request=request , template_name='detail.html' , context={'detail':dt})

def Product_list(request):
    prod_list = ProductList.objects.all()
    return render(request=request , template_name='ProductList.html' , context={"p_list":prod_list})
