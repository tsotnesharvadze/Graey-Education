from django.db import models
from django.utils.translation import gettext_lazy as _

from store.choices import GenderChoices


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.city} : {self.street_address}: {self.zip}'


class StoreToBook(models.Model):
    store = models.ForeignKey(to='store.Store', on_delete=models.CASCADE, related_name='store_to_books')
    book = models.ForeignKey(to='store.Book', on_delete=models.CASCADE, related_name='store_to_books')
    quantity = models.PositiveSmallIntegerField('Quantity', default=0)


class Store(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    location = models.OneToOneField('store.Location', on_delete=models.PROTECT, related_name='store')
    books = models.ManyToManyField(to='store.Book', blank=True, related_name='stores', through='store.StoreToBook')

    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Book Name", unique=True)
    created = models.DateTimeField(verbose_name="Added Date/Time", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated Date/Time", auto_now=True)
    author = models.ManyToManyField(to='store.Author', blank=True)

    class Meta:
        # unique_together = ('name', 'author')
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name

    def get_quantity(self):
        return f'რაოდენობაშია: 4'


class Author(models.Model):
    full_name = models.CharField("Full Name", max_length=255)
    age = models.PositiveSmallIntegerField("Age")
    gender = models.PositiveSmallIntegerField("Gender", choices=GenderChoices.choices, default=GenderChoices.Other)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.full_name

    def get_info(self):
        return f'Age: {self.age}'
