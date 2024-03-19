from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import TaskForm
from ..models import Event

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