from django.contrib import admin
from .models import Shop, Product, Review

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'type', 'created_at', 'updated_at')
    search_fields = ('name', 'address')
    list_filter = ('type', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'shop', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('shop', 'created_at', 'updated_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'content_type', 'object_id', 'created_at')
    search_fields = ('text',)
    list_filter = ('created_at', 'content_type')
