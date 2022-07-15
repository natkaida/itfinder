from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name="projects"),
    path('project-object/<str:pk>/', views.project, name="project"),
]