from django.urls import path

from store.views import store_listing, my_test_view, detail

app_name = 'store'

urlpatterns = [
    path('', store_listing, name='store_listing'),
    path('detail/<int:pk>/', detail, name='store_detail'),
    path('redirect/', my_test_view, name='my_test_view1'),
]