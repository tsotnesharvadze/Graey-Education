# from django.contrib.auth.views import LoginView
from django.urls import path

from user.views import user_registration, user_login, user_logout

app_name = 'user'

urlpatterns = [
    # path('', LoginView.as_view(
    #     template_name='user/login.html'
    # ), name='user_login'),
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('registration/', user_registration, name='user_registration'),
]
