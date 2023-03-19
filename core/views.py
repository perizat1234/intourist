from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def profile(request):
    user = request.user
    profile_obj = user.profile
    return render(request,'profile.html', {'profile':profile_obj})   
