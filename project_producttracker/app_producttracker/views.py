from math import prod
from django.shortcuts import render

from app_producttracker.forms import ProductCreateForm

from .models import Product
# Create your views here.
def product_index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products/index.html', context)

def product_create(request):
    template = 'products/create.html'
    product_form = ProductCreateForm
    if request.method == "POST":
        # creating product object
        product = Product()

        # assigning value to attributes
        product.title = request.POST.get("title")
        product.desc = request.POST.get("desc")
        product.price = request.POST.get("price")
        product.category = request.POST.get("category")
        product.quantity = request.POST.get("quantity")
        product.user_id = 1

        # storing product
        product.save()

        context = {"form": product_form, "msg_success": "Product Added"}
        return render(request, template, context)

    context = {"form": product_form}
    return render(request, template, context)