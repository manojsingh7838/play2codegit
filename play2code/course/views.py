from django.shortcuts import render


# Create your views here.
def alldoc(request):
    return render(request, "alldoc.html")
