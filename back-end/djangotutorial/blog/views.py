from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Post


def hello(request):
    return render(request, 'blog/hello.html', context={
        'posts': Post.objects.all()
    })


class PostView(TemplateView):
    queryset = Post.objects.all()
    template_name = 'blog/hello.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'posts': self.queryset
        }
