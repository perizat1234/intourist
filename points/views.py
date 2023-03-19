from django.shortcuts import render
from .models import Point

def points(requests):
    points_obj = Point.objects.all()
    return render(requests, 'points.html', {'points':points_obj} )
