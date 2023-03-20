from django.shortcuts import render

def homepage(request):
    return render(request, 'core/home.html')


def profile(request):
    user = request.user
    profile_obj = user.profile
    return render(request,'core/profile.html', {'profile':profile_obj})   
