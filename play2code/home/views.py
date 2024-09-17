from django.shortcuts import render


# Create your views here.
def homes(request):
    return render(request, "home.html")


def free(request):
    return render(request, "freelance.html")


def courses(request):
    return render(request, "course.html")
