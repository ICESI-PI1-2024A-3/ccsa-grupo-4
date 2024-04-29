from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from ..forms.taskForm import TaskForm
from ..models import Event
from ..models import Task


def create_task(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'GET':
        # Crear el formulario de tarea y establecer el evento predeterminado
        form = TaskForm(event_instance=event)
        return render(request, 'create_task.html', {'formForTask': form})
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.event = event
            new_task.save()
            return redirect("home")
        else:
            return render(request, "create_task.html", {
                "formForTask": form,
                'error': 'Por favor, digite valores válidos'
            })


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'GET':
        if request.user.is_superuser:
            form = TaskForm(instance=task)
        else:
            user_events = Event.objects.filter(user=request.user)
            form = TaskForm(instance=task)
            form.fields['event'].queryset = user_events
    else:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if not request.user.is_superuser:
                # Si el usuario no es superusuario, asigna la tarea al usuario actual automáticamente
                task.user = request.user
            task.save()
            return redirect('event_checklist', event_id=task.event.id)
        else:
            return render(request, "edit_task.html", {'taskId': task, 'form': form, 'error': "Error al intentar actualizar, intente de nuevo"})

    return render(request, "edit_task.html", {'taskId': task, 'form': form})


def delete_task(request, task_id):
    if request.user.is_superuser:
        task = get_object_or_404(Task, pk=task_id)
    else:
        task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('event_checklist', event_id=task.event.id)
