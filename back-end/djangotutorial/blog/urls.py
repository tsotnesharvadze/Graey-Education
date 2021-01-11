from django.urls import path

from blog.views import hello

urlpatterns = [
    path('hello/', hello)
]
