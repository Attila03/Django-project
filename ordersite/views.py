from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .forms import PizzaForm, RegistrationForm, UserLoginForm
from .models import Pizza, Topping, Cart, Customer
from .quote import get_quote
from .cart import add_base_pizza, add_custom_pizza, sessioncart_to_dbcart


class Homeview(View):

    def get(self, request, *args, **kwargs):
        quote, author = get_quote()
        context = {
            "quote": quote,
            "author": author
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
                    'request': request,
                    }
        return render(request, 'ordersite/Menu.html', context=context)


class AddToCartview(View):

    def get(self, request, *args, **kwargs):
        pizza_id = int(request.GET['pizza'])
        add_base_pizza(request, request.session["cart"], pizza_id)
        print(request.session["cart"])
        return HttpResponse()


class Orderview(View):

    def get(self, request,*args, **kwargs ):
        customer = request.user
        if not request.session.get('cart_created'):
            new_cart = Cart(customer=customer)
            new_cart.save()
            sessioncart_to_dbcart(request.session["cart"], new_cart, customer)
            request.session['cart_created'] = True
        return render(request, 'ordersite/Order.html')


class Customview(View):

    def get(self, request, *args, **kwargs):
        context = {
            'form': PizzaForm(),
        }
        return render(request, 'ordersite/Custom.html', context=context)

    def post(self, request):
        form = PizzaForm(request.POST)
        if form.is_valid():
            custom_pizza = form.save()
            add_custom_pizza(request, request.session["cart"], custom_pizza.id)
            print(request.session["cart"])
        return HttpResponse()


class Loginview(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'ordersite/Login.html',context=context)

    def post(self,request,*args,**kwargs):
        form = UserLoginForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request, user=user)
            request.session["cart"] = {"base": {}, "custom": {}, "total": 0}
            return redirect(reverse('Menu', args=('All',)))
        return render(request, 'ordersite/Login.html', context=context)


class Logoutview(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('Home'))


class Registerview(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'ordersite/Register.html', context={'form': RegistrationForm()})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            password = form.cleaned_data['password']
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)
            return redirect('/')
        return render(request, 'ordersite/Register.html',context={'form': form})


class Orderhistory(View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(username=request.user.username)
        carts = customer.get_carts()
        context = {"carts": carts}
        return render(request, 'ordersite/Orderhistory.html', context=context)
