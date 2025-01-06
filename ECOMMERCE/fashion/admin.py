from django.contrib import admin
from .models import FashionItem

@admin.register(FashionItem)
class FashionItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'stock_quantity')
    search_fields = ('name', 'brand', 'category')
    list_filter = ('brand', 'category')
