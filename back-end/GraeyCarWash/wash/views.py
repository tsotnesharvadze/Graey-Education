from django.db.models import Count
from django.shortcuts import render

from user.models import User


def base(request):

    return render(request=request, template_name='wash/washer-list.html', context={
        'washers': User.objects.filter(status=User.Status.washer.value).annotate(washed_count=Count('orders'))
    })
