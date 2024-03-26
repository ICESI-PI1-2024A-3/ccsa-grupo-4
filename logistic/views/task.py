from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from ..forms.taskForm import TaskForm
from ..models import Event
from ..models import Task

def create_task(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            user_events = Event.objects.all()
        else:
            # Obtener los eventos asociados al usuario actual
            user_events = Event.objects.filter(user=request.user)
        # Crear el formulario de tarea y filtrar los eventos asociados al usuario
        form = TaskForm()
        form.fields['event'].queryset = user_events
        return render(request, 'create_task.html', 
                      {'formForTask': form})
    else:
        try:
            if request.user.is_superuser:
                user_events = Event.objects.all()
            else:
                # Obtener los eventos asociados al usuario actual
                user_events = Event.objects.filter(user=request.user)
            form = TaskForm(request.POST)
            # Aplicar el filtro a los eventos en el formulario
            form.fields['event'].queryset = user_events
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.save()
                return redirect("home")
        except:
            return render(request, "create_task.html", {
                "formForTask": TaskForm,
                'error': 'Por favor, digite valores válidos'
            })

def edit_task(request, task_id):
    if request.method == 'GET':
        if request.user.is_superuser:
            # Aqui se obtiene el objeto y le indicamos que solo queremos el pk = event_id
            task = get_object_or_404(Task, pk=task_id)
            formForEditTask = TaskForm(instance=task)
        else:
            # Si no es el admin, se hace filtro para que no pueda editar las otras tasks
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            formForEditTask = TaskForm(instance=task)
        # El primer eventId,simplem   ente es el nombre de uan variable. El segundo task es el que se obtiene. El que se llama en el html es el que va entre comillas
        return render(request, "edit_task.html", {'taskId': task, 'form': formForEditTask})
    else:
        try:
            if request.user.is_superuser:
                task = get_object_or_404(Task, pk=task_id)
                # Obtiene los datos del formulario
                form = TaskForm(request.POST, instance=task)
            else:
                task = get_object_or_404(
                    Task, pk=task_id, user=request.user)
                form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('event_checklist', event_id = task.event.id)
        except ValueError:
            return render(request, "edit_task.html", {'tasktId': task, 'form': formForEditTask,
                                                       'error': "Error al intentar actualizar, intente de nuevo"})

def delete_task(request, task_id):
    if request.user.is_superuser:
        task = get_object_or_404(Task, pk=task_id)
    else:
        task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('event_checklist', event_id = task.event.id)

