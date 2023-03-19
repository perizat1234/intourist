from django.urls import path
from .views import points

urlpatterns = [
    path('', points, name= 'points-list'),
]