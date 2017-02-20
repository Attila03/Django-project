from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from .forms import PizzaForm
from .models import Pizza, Topping
# Create your views here.


class Allview(View):

    def get(self, request, *args, **kwargs):
        #print(request)
        P = Pizza.objects.filter(custom=False)
        T = Topping.objects.all()

        context ={
            'P': P,
            'T': T,
        }
        return render(request, 'ordersite/All.html', context=context)


class Vegview(View):

    def get(self, request, *args, **kwargs):
        P = Pizza.objects.all().filter(vegetarian=True,custom=False)
        T = Topping.objects.all()

        context = {
            'P': P,
            'T': T,
        }

        return render(request, 'ordersite/Veg.html', context = context)


class Nonvegview(View):
    def get(self, request, *args, **kwargs):
        P = Pizza.objects.all().filter(vegetarian=False, custom=False)
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


class Customview(View):

    def get(self, request, *args, **kwargs):
        #print(request)
        context ={
            'PF' : PizzaForm(),
        }
        return render(request, 'ordersite/Custom.html', context=context)

    def post(self, request):
        #print(request)
        #print(type(request))
        form = PizzaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            P = Pizza(name=cd['name'])
            P.save()
            P.toppings.add(*cd['toppings'])
            # for topping in cd['toppings']:
            #     P.toppings.add(topping)
        return render(request, 'ordersite/Pizzaorder.html', context={'pizza':P})


