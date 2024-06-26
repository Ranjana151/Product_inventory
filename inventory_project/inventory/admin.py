from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Product, ProductAdmin)
