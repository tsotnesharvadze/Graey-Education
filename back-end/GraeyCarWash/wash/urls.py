from django.urls import path

from wash.views import base

urlpatterns = [
    path('base/', base)
]
