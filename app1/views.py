
from django.shortcuts import render
from .models import Category, Suppliers, Products

def product_list(request):
    # GET parametrlar
    cat_id = request.GET.get('category')
    sup_id = request.GET.get('supplier')

    products = Products.objects.all()

    # Category filter birinchi ustunlik beradi
    if cat_id:
        products = products.filter(category_id=cat_id)
    elif sup_id:
        products = products.filter(supplier_id=sup_id)

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'suppliers': Suppliers.objects.all(),
        'selected_category': cat_id,
        'selected_supplier': sup_id,
        'name': "Productlar ro‘yxati",
    }

    return render(request, 'product.html', context)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def supplier_list(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'supplier.html', {'suppliers': suppliers})
