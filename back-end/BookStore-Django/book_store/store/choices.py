from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    '''(
        (1, 'Male',),
        (2, 'Female',),
        (3, 'Other1',),
        )
    '''
    Male = 1
    Female = 2
    Other = 3
