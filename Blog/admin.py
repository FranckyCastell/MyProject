from django.contrib import admin
from .models import Blog
# Register your models here.


class BlogProduct(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']  # READ FIELDS
    list_display = ['title', 'author']  # COL DATA
    search_fields = ['title']  # SEARCH DATA
    list_filter = ['author']  # FILTER


admin.site.register(Blog, BlogProduct)
