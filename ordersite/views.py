from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .forms import PizzaForm, RegistrationForm, UserLoginForm
from .models import Pizza, Topping, Cart
from .quote import get_quote
# Create your views here.

class Homeview(View):

    def get(self, request, *args, **kwargs):
        quote, author = get_quote()
        context = {
            "quote" : quote,
            "author" : author
        }
        return render(request, 'ordersite/Home.html', context=context)


class Menuview(View):

    def get(self, request, menu_type=None):
        pizza_qs = Pizza.objects.filter(custom=False)
        if menu_type == 'Veg':
            pizza_qs = pizza_qs.filter(vegetarian=True, custom=False)
        elif menu_type == 'Nonveg':
            pizza_qs = pizza_qs.filter(vegetarian=False, custom=False)
        context = {
                    'pizza_qs': pizza_qs,
                    'request' : request,
                    }

        return render(request, 'ordersite/Menu.html', context=context)


class Orderview(View):

    def get(self, request,*args, **kwargs ):
        customer = get_object_or_404(Customer, username=request.user.username)
        if not request.session.get('cart_created'):
            new_cart = Cart(customer=customer)
            new_cart.save()
            for pizza in request.session['cart']['base']:
                new_cart.pizzas.add(get_object_or_404(Pizza,name=pizza[0]))
            for pizza in request.session['cart']['custom']:
                new_pizza = Pizza(name=pizza[0])
                new_pizza.save()
                for topping in pizza[2]:
                    new_pizza.toppings.add(get_object_or_404(Topping, name=topping))
                new_cart.pizzas.add(new_pizza)
            request.session['cart_created']=True

        return render(request, 'ordersite/Order.html')


class Helpview(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'ordersite/Help.html')


class Customview(View):

    def get(self, request, *args, **kwargs):
        context ={
            'form' : PizzaForm(),
        }
        return render(request, 'ordersite/Custom.html', context=context)

    def post(self, request):
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza_name = form.cleaned_data['name']
            pizza_toppings = [topping.name for topping in form.cleaned_data['toppings']]
            pizza_cost = sum(topping.cost for topping in form.cleaned_data['toppings'])
            request.session['cart']['custom'].append((pizza_name, pizza_cost, pizza_toppings))
            request.session['total'] += int(pizza_cost)
            request.session.modified = True
        return HttpResponse()



class Registerview(View):

    def get(self, request, *args, **kwargs):
        context = {
            'form' : RegistrationForm(),
        }

        return render(request, 'ordersite/Register.html', context=context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            password = form.cleaned_data['password']
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)
            return redirect('/')
        context = {
            'form' : form,
        }

        return render(request, 'ordersite/Register.html',context=context)

class Loginview(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {'form':form}
        return render(request, 'ordersite/Login.html',context=context)

    def post(self,request,*args,**kwargs):
        form = UserLoginForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request, user=user)
            request.session["cart"] = {'base':[], 'custom':[]}
            request.session['total'] = 0
            return redirect(reverse('Menu', args=('All',)))
        return render(request, 'ordersite/Login.html', context=context)

'''
Session Cart format
 Cart = {
        'base': [[pizza_name, pizza_cost],....] ,
        'custom': [[pizza_name, pizza_cost, [topping.name,...]],...],
    }
'''


class Logoutview(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('Home'))


class AddToCartview(View):

    def get(self, request, *args, **kwargs):
        pizza_name, pizza_cost = request.GET['pizza'].split('_')
        request.session['cart']['base'].append([pizza_name, pizza_cost])
        request.session['total'] += int(pizza_cost)
        request.session.modified = True
        return HttpResponse()