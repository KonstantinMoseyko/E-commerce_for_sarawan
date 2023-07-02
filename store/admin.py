from django.contrib import admin

from .models import Category, SubCategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description',)
    prepopulated_fields = {'slug': ('name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'category',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'price', 'subcategory',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
