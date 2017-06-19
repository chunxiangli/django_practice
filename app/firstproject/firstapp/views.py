from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from numpy import *

@api_view()
def api_root(request):
    """
    The root of all APIs, serves as a basic presentation of the APIs aviliable, 
    however needs manual additions of the functions.
    reverse() serves as a url call to each function views.
    """
    return Response({
        'hello_world': reverse('hello_world', request=request),
        'divide': reverse('divide', request=request),
        'multiply': reverse('multiply', request=request),
        'add': reverse('add', request=request),
    })

@api_view()
def hello_world(request):
    """
    An example api, this part of text will be visible when entering /hello_world.
    """
    return Response({"message": "Hello, world!"})

@api_view()
def add(request):
    """
    An addition function. 
    add(
        a: int,
        b: int,
        ret: int
    )
    example call: **whatever_host**/add/?a=1&b=1
    should return a json looks like:
    {'function': 'add','result': 2}
    """
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return Response({'function': 'add','result': first_number + second_number})
    except Exception as e:
        return Response({'function': 'add','result': 'there was an error ' + str(e)})
