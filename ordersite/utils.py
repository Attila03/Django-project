from .models import Cart, Pizza, Customer, Topping


def sessioncart_to_dbcart(sessioncart, dbcart, customer):
    '''Converts the session cart dictionary into db model Cart object and associates it with a customer'''
    for idx in sessioncart["base"]:
        dbcart.pizzas.add(Pizza.objects.get(pk=int(idx)))
    for idx in sessioncart["custom"]:
        pizza = Pizza.objects.get(pk=int(idx))
        pizza.customer = customer
        pizza.save()
        dbcart.pizzas.add(pizza)
    dbcart.save()


