from django.shortcuts import render

# Create your views here.
# src/projects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from tasks.forms import TaskForm  # usamos el form de tasks
from tasks.models import Task

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()  # related_name='tasks'
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks,
    })

def project_create(request):
    from .forms import ProjectForm
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.owner = request.user
            proj.save()
            messages.success(request, 'Project creado.')
            return redirect('project_detail', pk=proj.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def project_update(request, pk):
    from .forms import ProjectForm
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project actualizado.')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project eliminado.')
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

# Vista para crear tarea desde un proyecto (flujo A).
def task_create_from_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project            # asigna automáticamente el proyecto
            task.assigned_to = request.user   # asigna al usuario logueado
            task.save()
            messages.success(request, 'Task creada en el proyecto.')
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})
