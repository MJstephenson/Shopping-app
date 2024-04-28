from django.contrib import admin
from .models import Category, AlcoholType, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name',)
    ordering = ('name',)


class AlcoholTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'sku', 'category', 'alcohol_type', 'price', 'rating',
        'alcohol_content', 'volume', 'country_of_origin', 'year_of_production',
        'stock', 'image', 'new_arrival', 'deal', 'clearance'
    )

    list_filter = ('new_arrival', 'deal', 'clearance')

    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(AlcoholType, AlcoholTypeAdmin)
admin.site.register(Product, ProductAdmin)
