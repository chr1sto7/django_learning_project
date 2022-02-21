from django.urls import path
from . import views


# these are our app urls which correspond to our routing functions defined in views
# we must name our variable urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
]
