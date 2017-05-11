from .models import Pizza, Topping

'''
    Cart = {
        "base" : {
            "id" : { "count" : 1, "cost": 120, "veg":True},
            ...
        },
        "custom" : {
            "id" : {"name": "mypizza", "count":2, "cost":230, "toppings": ("onion", "chicken"), "veg":False},
             .....
        }
        "total" : 0
    }
'''


def add_base_pizza(request, cart, pizza_id):
    idx = str(pizza_id)
    pizza = Pizza.objects.get(pk=pizza_id)
    if idx in cart["base"]:
        cart["base"][idx]["count"] += 1
        cart["base"][idx]["cost"] += pizza.cost
    else:
        pizza = Pizza.objects.get(pk=pizza_id)
        cart["base"][idx] = {"name": pizza.name, "count": 1, "cost": pizza.cost, "veg": pizza.vegetarian}
    cart["total"] += pizza.cost
    request.session.modified = True


def add_custom_pizza(request, cart, pizza_id):
    idx = str(pizza_id)
    pizza = Pizza.objects.get(pk=pizza_id)
    if idx in cart["custom"]:
        cart["custom"][idx]["count"] += 1
        cart["custom"][idx]["cost"] += pizza.cost
    else:
        cart["custom"][idx] = {"name": pizza.name, "count": 1, "cost": pizza.cost, "veg": pizza.vegetarian,
                                 "toppings": [topping.name for topping in pizza.toppings.all()]}
    cart["total"] += pizza.cost
    request.session.modified = True



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
