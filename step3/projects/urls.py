from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<slug:project_slug>/', views.project, name="project"),
    path('tag/<slug:tag_slug>', views.projects_by_tag, name="tag"),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]