import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

from store.models import Store


def store_listing(request):

    stores = Store.objects.select_related('location').prefetch_related("books")
    # locations = Location.objects.prefetch_related('store')
    return render(
        request,
        "store_listing.html",
        context={
            "stores": stores,
            "time_now": datetime.datetime.now().isoformat(),
        }
    )
    # data = [{"title": store.title} for store in stores]
    # return JsonResponse(data, safe=False)

    # return redirect('store:my_test_view1')
    # return redirect('http://google.com')
    # return redirect('/redirect/')


def my_test_view(request):
    return HttpResponse('redirect text')


def detail(request, pk):
    store = get_object_or_404(Store, id=pk)
    # raise Http404('ალოოო')
    return render(request, 'store_detail.html', context={
        'store': store
    })
