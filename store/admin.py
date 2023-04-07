from django.contrib import admin
from store.models import Product, Variation, ReviewRating

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'old_price', 'stock','category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category',  'variation_value', 'created_date', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category',  'variation_value')

    
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('user','product', 'subject', 'review','rating','ip','created_at', 'updated_at', 'status')
    list_filter = ('user', 'product', 'rating')
    list_display_links = ('user','product','subject', 'review')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
