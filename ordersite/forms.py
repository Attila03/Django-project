from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Pizza, Customer


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['toppings', 'name']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple,
        }


class RegistrationForm(forms.ModelForm):
    email2 = forms.EmailField(
        label='Confirm Email',
        widget=forms.EmailInput(attrs={'placeholder':'abc@gmail.com'}),
    )
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = Customer

        fields = ['username', 'email', 'email2','password', 'password2']

        widgets = {'password': forms.PasswordInput,
                   'email': forms.EmailInput(attrs={'placeholder':'abc@gmail.com',}),
                    }

        help_texts = {'username': None,}



    def clean_email2(self):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['email2']
        if email != email2 :
            raise forms.ValidationError("Email is not  matching!")
        return email


    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Passwords not matching')
        return password


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        print(username, password)
        user = User.objects.filter(username=username)
        if not user:
            raise forms.ValidationError('Username does not exist')
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Incorrect password for the username.')
        return super(UserLoginForm, self).clean(*args, **kwargs)








