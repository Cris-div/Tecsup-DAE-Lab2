from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),                 # /projects/
    path('new/', views.project_create, name='project_create'),         # /projects/new/
    path('<int:pk>/', views.project_detail, name='project_detail'),    # /projects/1/
    path('<int:pk>/edit/', views.project_update, name='project_update'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),

    # ruta para crear tarea desde un proyecto (flujo A)
    path('<int:project_id>/tasks/new/', views.task_create_from_project, name='task_create_project'),
]
