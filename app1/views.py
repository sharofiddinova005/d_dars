from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import News, Category, Suppliers, Products
from .forms import NewsForm, CategoryForm, SupplierForm, ProductForm


# ---------------- NEWS ----------------
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


class HomeNews(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'


def del_new(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('home')


# ---------------- CATEGORY ----------------
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Kategoriya qo‘shish'})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


# ---------------- SUPPLIER ----------------
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Supplier qo‘shish'})


def supplier_list(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})


# ---------------- PRODUCT ----------------
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Product qo‘shish'})


def product_list(request):
    products = Products.objects.all()
    return render(request, 'product_list.html', {'products': products})
