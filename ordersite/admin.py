from django.contrib import admin

from .models import Topping, Pizza, Customer, Cart

# Register your models here.

admin.site.register(Topping)


# class PizzaAdmin(admin.ModelAdmin):
#     def save_related(self, request, form, formsets, change):
#         super(PizzaAdmin, self).save_related(request,form,formsets,change)
#         current = form.instance
#         current.cost = 0
#         for topping in current.toppings.all():
#             current.cost += topping.cost
#             if topping in NONVEG:
#                 current.vegeterian = False
#         form.instance.save(update_fields=['cost', 'vegeterian'])

admin.site.register(Pizza)
admin.site.register(Customer)
admin.site.register(Cart)
