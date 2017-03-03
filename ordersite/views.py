from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views import View
from .forms import PizzaForm, RegistrationForm, UserLoginForm
from .models import Pizza
# Create your views here.


class Homeview(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'ordersite/Home.html')


class Menuview(View):

    def get(self, request, menu_type=None):
        pizza_qs = Pizza.objects.filter(custom=False)
        if menu_type == 'Veg':
            pizza_qs = pizza_qs.filter(vegetarian=True, custom=False)
        elif menu_type == 'Nonveg':
            pizza_qs = pizza_qs.filter(vegetarian=False, custom=False)
        context = { 'pizza_qs': pizza_qs, }

        return render(request, 'ordersite/Menu.html', context=context)


class Pizzaorderview(View):

    def get(self, request, pizza_name=None,menu_type=None, *args, **kwargs ):
        print(menu_type)
        context ={
            'pizza' : get_object_or_404(Pizza, name=pizza_name),
        }
        return render(request, 'ordersite/Pizzaorder.html', context=context)


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
            cd = form.cleaned_data
            P = Pizza(name=cd['name'])
            P.save()
            P.toppings.add(*cd['toppings'])
        return render(request, 'ordersite/Pizzaorder.html', context={'pizza':P})


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
            return redirect('/')
        return render(request, 'ordersite/Login.html', context=context)

class Logoutview(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        print(request.user)
        return redirect('/')

