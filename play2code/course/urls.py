from django.urls import path
from . import views

urlpatterns = [
    path("", views.alldoc, name="all-doc"),
]
