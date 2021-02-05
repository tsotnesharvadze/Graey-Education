from django.urls import path

from wash.views import washer_list_view, washer_detail, contact, make_order

app_name = 'wash'

urlpatterns = [
    path('washers/', washer_list_view, name='washer-list'),
    path('washers/<int:pk>/', washer_detail, name='washer-detail'),
    path('contact/', contact, name='contact'),
    path('order/<int:pk>/', make_order, name='order'),
]
