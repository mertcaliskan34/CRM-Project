from django import forms
from django.contrib import admin

from .models import Record, Product, Review, Order

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    
    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = '__all__'
            widgets = {
                'description': forms.Textarea(attrs={'rows': 8, 'cols': 80}),
            }
    form = ProductForm

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description',)
    search_fields = ('name',)
    inlines = [ReviewInline]
    
    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = '__all__'
            widgets = {
                'description': forms.Textarea(attrs={'rows': 8, 'cols': 80}),
            }
    form = ProductForm

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'status', 'creation_date')
    list_filter = ('customer', 'status',)
    
admin.site.register(Record)

admin.site.register(Product, ProductAdmin)

admin.site.register(Order, OrderAdmin)