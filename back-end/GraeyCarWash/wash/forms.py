from django import forms
from django.forms import EmailField, CharField

from wash.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('wash_type', 'note', 'car')


class ContactForm(forms.Form):
    email = EmailField()
    body = CharField()
