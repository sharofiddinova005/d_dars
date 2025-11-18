from django.urls import path
from .views import product_list, category_list, supplier_list

urlpatterns = [
    path('products/', product_list, name='products'),
    path('categories/', category_list, name='categories'),
    path('suppliers/', supplier_list, name='suppliers'),
]
