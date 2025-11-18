from django.contrib import admin
from .models import *
from .models import Category, Products, Suppliers


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_ed', 'updated_ed')
    list_display_links = ['title','created_ed','id']
    search_fields = ['title']


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']




