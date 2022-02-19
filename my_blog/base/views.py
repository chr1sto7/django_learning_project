"""views are the complex business logic e.g. CRUD ops"""

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    print(request)  # response is passed implicitly from the http request to our app
    return HttpResponse('Hello World')


def room(request):
    print(request)
    return HttpResponse('ROOM')