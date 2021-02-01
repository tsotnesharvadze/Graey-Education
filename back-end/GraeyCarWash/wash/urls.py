from django.urls import path

from wash.views import washer_list_view, washer_detail

app_name = 'wash'

urlpatterns = [
    path('washers/', washer_list_view, name='washer-list'),
    path('washers/<int:pk>/', washer_detail, name='washer-detail'),
]
