from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "CATEGORY"
        verbose_name_plural = "CATEGORIES"
        ordering = ['id']


class Suppliers(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    company = models.CharField(max_length=150)
    address = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.company})"

    class Meta:
        verbose_name = "SUPPLIER"
        verbose_name_plural = "SUPPLIERS"
        ordering = ['-created_ed']


class Products(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "PRODUCT"
        verbose_name_plural = "PRODUCTS"
        ordering = ['-created_ed']

class News(models.Model):
    title=models.CharField(max_length=50)
    context=models.TextField(blank=True)
    created_ed=models.DateTimeField(auto_now_add=True)
    updated_ed=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    is_bool=models.BooleanField(default=True)
    views=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title} - {self.views}"

    class Meta:
        verbose_name="NEW"
        verbose_name_plural="NEWS"
        ordering=['-created_ed']
