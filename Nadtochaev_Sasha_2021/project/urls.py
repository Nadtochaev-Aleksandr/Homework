from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('project_app/', views.project_page),
]
