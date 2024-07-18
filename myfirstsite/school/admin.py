from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slag" : ("prod_name",)}

admin.site.register(Product, ProductAdmin)

