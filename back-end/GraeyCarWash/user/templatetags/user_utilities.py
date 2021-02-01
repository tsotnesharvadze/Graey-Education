from datetime import date

from django import template

# DateField

register = template.Library()


@register.filter(name='is_adult')
def is_adult(birthdate: 'date', threshold: int):
    today = date.today()
    age = today.year - birthdate.year - (
            (today.month, today.day) < (birthdate.month, birthdate.day)
    )
    return age > threshold


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    timezone: 'date' = context['timezone']
    return timezone.strftime(format_string)
