from django.core.exceptions import ValidationError


def validate_phone(value):
    if len(value) != 9:
        raise ValidationError('ნომერი უნდა იყოს 9 ნიშნა')