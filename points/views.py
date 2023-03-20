from django.shortcuts import render,redirect
from .models import Point
from .forms import PointForm

def points(requests):
    points_obj = Point.objects.all()
    return render(requests, 'points/points.html', {'points':points_obj} )

def create(request):
    if request.method == "POST":
       point_form = PointForm(request.POST)
       if point_form.is_valid():
        point_form.save()
        return redirect(points)
    point_form = PointForm()
    return render(request, 'points/form.html', {'point_form': point_form} )  

def point(request,id):
    point_obj = Point.objects.get(id=id)
    return render(request, 'points/point.html',{'point_obj':point_obj})

def edit_place(request,id):
    point_obj = Point.objects.get(id=id)
    if request.method == "POST":
       point_form = PointForm(data = request.POST, instance=point_obj)
       if point_form.is_valid():
        point_form.save()
        return redirect(point,id = id)
    point_form = PointForm(instance=point_obj)
    return render(request, 'points/form.html', {'point_form':point_form})


def delete_place(request,id):
    point_obj = Point.objects.get(id=id)
    point_obj.delete()
    return redirect(points)