from django.urls import path

from user.views import user_registration, user_login

app_name = 'user'

urlpatterns = [
    path('', user_login, name='user_login'),
    path('registration/', user_registration, name='user_registration'),
]