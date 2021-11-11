from django.shortcuts import render
from .models import Category, Product

# Create your views here.


def category(request, id):

    # FILTER PRODUCTS BY 'CATEGORY ID' ( DATABASE_ATTRIBUTE - PARAMETER )
    products = Product.objects.filter(category_id=id)

    context = {'products': products}
    return render(request, 'Shop/category.html', context)
