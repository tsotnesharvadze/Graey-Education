from django.contrib.auth.decorators import login_required as lr
from django.urls import path

from wash.views import washer_list_view, washer_detail

app_name = 'wash'

urlpatterns = [
    path('', lr(washer_list_view), name='washer-list'),
    path('<int:pk>/', washer_detail, name='washer-detail'),
]
