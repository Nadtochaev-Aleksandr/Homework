from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('project_app/', views.project_page),
    path('', views.project_index, name="project_index"),
    path('<int:pk>/', views.project_detai, name="project_detail")
]
