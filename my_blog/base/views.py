"""views are the complex business logic e.g. CRUD ops"""

from django.shortcuts import render

# this is passed as our context param for use in a rendered html template
rooms = [
    {'id': 1, 'name': 'Python Project Ideas', 'content': True},
    {'id': 2, 'name': 'Learning Wishlist', 'content': True},
    {'id': 3, 'name': 'Project Status', 'content': True},
    {'id': 4, 'name': 'Test Header', 'content': False}
]


def home(request):  # request response is passed implicitly from the http request to our app
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)  # this renders our html template as a http response


def room(request):
    return render(request, 'base/room.html')  # this renders our html template as a http response
