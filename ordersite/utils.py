from .models import Cart, Pizza, Customer, Topping
from django.shortcuts import get_object_or_404

'''
Session Cart format
 Cart = {
        'base': [[pizza_name, pizza_cost],....] ,
        'custom': [[pizza_name, pizza_cost, [topping.name,...]],...],
    }
'''

def sessioncart_to_dbcart(sessioncart, dbcart):
    '''Converts the session cart dictionary into db model Cart object and associates it with a customer'''
    for pizza in sessioncart['base']:
        dbcart.pizzas.add(get_object_or_404(Pizza, name=pizza[0]))
    for pizza in sessioncart['custom']:
        new_pizza = Pizza(name=pizza[0])
        new_pizza.save()
        for topping in pizza[2]:
            new_pizza.toppings.add(get_object_or_404(Topping, name=topping))
        dbcart.pizzas.add(new_pizza)

def dbcart_to_sessioncart(dbcart):
    '''COnverts db model Cart object to session cart dictionary'''
    pass