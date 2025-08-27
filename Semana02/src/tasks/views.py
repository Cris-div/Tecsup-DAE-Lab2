from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from projects.models import Project  # si necesitas usar Project en lógica global


def task_list(request,  project_id=None):
    tasks = Task.objects.all()
    
    # Filtros opcionales
    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')
    project_filter = request.GET.get('project')
    
    if project_id:
        # Si vengo desde un proyecto específico, filtro las tareas
        tasks = tasks.filter(project_id=project_id)
    
    if status_filter and status_filter != 'all':
        tasks = tasks.filter(status=status_filter)
    
    if priority_filter and priority_filter != 'all':
        tasks = tasks.filter(priority=priority_filter)
    
    projects = Project.objects.all()  # para el select en la UI (opcional)

    
    context = {
        'tasks': tasks,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'project_filter': project_filter,
        'projects': projects,
        'project_id': project_id,  # 🔑 lo pasamos al template

    }
    
    return render(request, 'tasks/task_list.html', context)

def task_create(request):
    # creación *global*: si quieres permitirla
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # No fijamos task.project aquí porque este formulario global puede incluir project
            # O si tu TaskForm excluye project, entonces esto creará tareas sin proyecto (evítalo)
            task.assigned_to = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
