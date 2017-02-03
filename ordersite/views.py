from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.

from .models import Pizza, Topping

class Allview(View):

    def get(self, request, *args, **kwargs):
        P = Pizza.objects.all()
        T = Topping.objects.all()

        context ={
            'P': P,
            'T': T,
        }
        return render(request, 'ordersite/All.html', context=context)

class Vegview(View):

    def get(self, request, *args, **kwargs):
        P = Pizza.objects.all().filter(vegetarian=True)
        T = Topping.objects.all()

        context = {
            'P': P,
            'T': T,
        }

        return render(request, 'ordersite/Veg.html', context = context)

class Nonvegview(View):
    def get(self, request, *args, **kwargs):
        P = Pizza.objects.all().filter(vegetarian=False)
        T = Topping.objects.all()

        context = {
            'P': P,
            'T': T,
        }

        return render(request, 'ordersite/Nonveg.html', context=context)

class Homeview(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'ordersite/Home.html')

class Pizzaorderview(View):

    def get(self, request, pizza_name=None, *args, **kwargs ):
        context ={
            'pizza' : get_object_or_404(Pizza, name=pizza_name),
        }
        return render(request, 'ordersite/Pizzaorder.html', context=context)

class Helpview(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'ordersite/Help.html')

