from django.urls import path

from blog.views import PostView, hello

urlpatterns = [
    path('hello/', hello),
    path('hello/', PostView.as_view())
]
