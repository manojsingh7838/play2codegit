# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homes, name="home-page"),
    path("freelancer/", views.free, name="freelancer-page"),
    path("courses/", views.courses, name="freelancer-page"),
    path("contact/", views.contact_view, name="contact"),
    path("profiles/", views.profile_view, name="profiles"),
]
