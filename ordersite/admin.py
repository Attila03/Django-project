from django.contrib import admin

from .models import Topping, Pizza, Customer, Cart

# Register your models here.


admin.site.register(Topping)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    list_filter = ('vegetarian', 'custom')

admin.site.register(Pizza, PizzaAdmin)


# class CustomerInline(admin.TabularInline):
#     model = Customer
#
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'last_modified')
    fields = ['customer', 'pizzas']

class CartInline(admin.TabularInline):
    model = Cart

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CartInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
