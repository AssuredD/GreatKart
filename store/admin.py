from django.contrib import admin
from django.utils.html import format_html
import admin_thumbnails
from store.models import Product, Variation, ReviewRating, ProductGallery

# Register your models here.


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'old_price', 'stock','category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGalleryInline]


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
admin.site.register(ProductGallery)
