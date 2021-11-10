from django.contrib import admin
from .models import Category, Product

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']  # READ FIELDS
    list_display = ['name', 'price', 'category']  # COL DATA
    search_fields = ['name', 'category__name']  # SEARCH DATA
    list_filter = ['category__name']  # FILTER


admin.site.register(Category)
admin.site.register(Product, AdminProduct)
