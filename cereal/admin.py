from django.contrib import admin
from .models import ProductModel, ProductCategory
# Register your models here
admin.site.register(ProductModel)
admin.site.register(ProductCategory)