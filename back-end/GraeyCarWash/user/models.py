from decimal import Decimal

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from django.db.models import IntegerChoices
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        validate_email(email)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('birthdate', timezone.now())
        extra_fields.setdefault('image', "profiles/placeholder.jpg")
        extra_fields.setdefault('salary', 0)
        extra_fields.setdefault('phone_number', '0')
        extra_fields.setdefault('status', 3)
        extra_fields.setdefault('hire_date', timezone.now())
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    birthdate = models.DateField(verbose_name=_('Birth Date'), )
    image = models.ImageField(verbose_name=_("Image"), upload_to='profiles')
    salary = models.DecimalField(
        max_digits=8, decimal_places=2,
        verbose_name=_('Salary'), help_text='in Lari / % (if being washer )',
        default=Decimal(0)  # @TODO: Optimize
    )
    phone_number = models.CharField(max_length=50, verbose_name=_('Phone Number'))
    hire_date = models.DateField(auto_now_add=True, verbose_name=_("Hire Date"))

    class Status(IntegerChoices):
        customer = 1, _("Customer")
        washer = 2, _("Washer")
        manager = 3, _("Manager")

    status = models.PositiveSmallIntegerField(choices=Status.choices)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
