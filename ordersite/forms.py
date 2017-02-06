from django import forms

from .models import Pizza, Topping


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['toppings', 'name']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple,
        }