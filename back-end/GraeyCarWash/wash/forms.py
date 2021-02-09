from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.forms import EmailField, CharField, Textarea, ModelChoiceField, TextInput

from wash.models import Order, Car, WashType
from typing import Optional

from wash.validators import validate_phone


class OrderForm(forms.ModelForm):
    note = CharField(widget=Textarea(attrs={
        'id': 'icon_prefix2',
        'class': 'materialize-textarea'
    }), validators=[MaxLengthValidator(150)])
    car = ModelChoiceField(empty_label='აირჩიე მანქანა', queryset=Car.objects.all())
    wash_type = ModelChoiceField(queryset=WashType.objects.all(), empty_label='აირჩიე რეცხვის ტიპი')
    start_date_day = CharField(widget=TextInput(attrs={
        'class': 'datepicker'
    }), validators=[RegexValidator(
        r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](21|20)\d\d$',
        message='ფორმატი უნდა იყოს: dd/mm/yyyy'
    )])
    start_date_time = CharField(widget=TextInput(attrs={
        'class': 'timepicker'
    }), validators=[RegexValidator(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', message='ფორმატი უნდა იყოს: MM:HH')])

    class Meta:
        model = Order
        fields = ('car', 'wash_type', 'note', 'start_date_day', 'start_date_time',)


class ContactForm(forms.Form):
    email = EmailField()
    body = CharField()
    # phone = CharField(validators=[MaxLengthValidator(9), MinLengthValidator(9)])
    phone = CharField(validators=[validate_phone])

    @staticmethod
    def clean_phone(value: Optional[str]):
        '''
            +   995-634-34-34-34
            634343434
        '''
        if value is None:
            return value
        value = value.replace('-', '').strip('+ ')
        return value
