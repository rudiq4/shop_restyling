from django.contrib import admin
from .models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'created', 'text']


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'price',
        'available', 'created', 'updated'
    ]
    list_editable = [
        'price', 'available'
    ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)

