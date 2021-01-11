from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


class MyJsonResponse(JsonResponse):

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs):
        data['meta'] = 'me'
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)


def hello(request):
    time = datetime.now().isoformat(' ')

    return MyJsonResponse(
        {
            'time': time,
            'items': [
                {
                    'username': 'Misho'
                },
                {
                    'username': 'Tsotne'
                },
            ]
        }
    )
    # return render(request, 'blog/hello.html', context={
    #     'time': time,
    #     'items': [
    #         {
    #             'username': 'Misho'
    #         },
    #         {
    #             'username': 'Tsotne'
    #         },
    #     ]
    # })
