from django.shortcuts import render,redirect,HttpResponse
from .models import Point, Feedback
from .forms import PointForm,FeedbackForm
from django.views.generic import FormView, DetailView

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
    try:
       point_obj = Point.objects.get(id=id)
       return render(request, 'points/point.html',{'point_obj':point_obj})

    except Point.DoesNotExist as e:
        return HttpResponse(f'Not found: {e}', status = 404)

      
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



class FeedBackView(FormView):
    template_name = 'points/feedback_form.html'
    form_class = FeedbackForm
    success_url = '/points/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FeedBackDetailView(DetailView):
    queryset = Feedback.objects.all()  
    template_name = 'points/feedback.html'    




