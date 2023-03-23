from django.shortcuts import render
from django.views.generic import TemplateView

# def homepage(request):
#     return render(request, 'core/home.html')

class HomeView(TemplateView):
    template_name = 'core/home.html'

def profile(request):
    user = request.user
    profile_obj = user.profile
    return render(request,'core/profile.html', {'profile':profile_obj})   
