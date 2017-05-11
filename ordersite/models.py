from django.db import models
from django.contrib.auth.models import AbstractUser, User

from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed


class Customer(User):

    class Meta:
        proxy=True

    def get_carts(self):
        return self.cart_set.all()


class Topping(models.Model):
    TOPPING_CHOICES = (
        ('VEG', (
            ('Black Olives','Black Olives'),
            ('Paneer','Paneer'),
            ('Mushroom','Mushroom'),
            ('Capsicum','Capsicum'),
            ('Golden Corn','Golden Corn'),
            ('Jalapeno','Jalapeno'),
            ('Fresh Tomato','Fresh Tomato'),
            ('Red Pepper','Red Pepper'),
            ('Red Paprika', 'Red Paprika'),
        )
        ),
        ('NON-VEG', (
            ('Barbeque Chicken','Barbeque Chicken'),
            ('Spicy Chicken','Spicy Chicken'),
            ('Chunky Chicken','Chunky Chicken'),
            ('Chicken Salami','Chicken Salami'),
            ('Chicken Rashers','Chicken Rashers'),
        )
         )
    )

    name = models.CharField(max_length=50,blank=False, choices=TOPPING_CHOICES, unique=True)
    cost = models.IntegerField()
    vegetarian = models.BooleanField(default=True)

    def __str__(self):
        return "{}  -  {}".format(self.name, self.cost)


class Pizza(models.Model):
    name = models.CharField(max_length=50,blank=False)
    cost = models.IntegerField(blank=True, default=0)
    toppings = models.ManyToManyField(Topping, blank=True)
    vegetarian = models.BooleanField(blank=True, default=True)
    custom = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, null=True)

    def total_cost(self):
        return sum(topping.cost for topping in self.toppings.all())

    def __str__(self):
        return self.name

    @property
    def getimageurl(self):
        return '/img/{}.jpg'.format(self.name)


@receiver(m2m_changed, sender=Pizza.toppings.through)
def update_pizza(sender, **kwargs):
    current = kwargs['instance']
    current.cost = 0
    for topping in current.toppings.all():
        current.cost += topping.cost
    current.vegetarian = all(topping.vegetarian for topping in current.toppings.all())
    current.save()


class Cart(models.Model):
    customer = models.ForeignKey(Customer)
    pizzas = models.ManyToManyField(Pizza, blank=True)
    last_modified = models.DateTimeField(auto_now=True)


# Cannot use Manager 'objects' on instances of Model, can only be used on the Model class itself.

    # def save(self, *args, **kwargs):
    #     super(Pizza, self).save(*args, **kwargs)
    #     topping_qs = self.toppings.all()
    #     self.cost = 0
    #     for topping in topping_qs:
    #         self.cost += topping.cost
    #         if topping.name in NONVEG:
    #             self.vegeterian = False

# @receiver(post_save,sender=Pizza)
# def update_pizza(sender, **kwargs):
#     current = kwargs.get('instance')
#     current.cost = 0
#     for t in current.toppings.all():
#         current.cost += t.cost
#     current.vegetarian = all(t.vegetarian for t in current.toppings.all())