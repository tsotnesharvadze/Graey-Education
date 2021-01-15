from django.shortcuts import render

from blog.models import Post


def hello(request):
    return render(request, 'blog/hello.html', context={
        'posts': Post.objects.all()
    })

