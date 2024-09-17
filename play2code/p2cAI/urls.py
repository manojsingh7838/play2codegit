# play2code/urls.py
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.ask_question, name="ask_question"),
]
