from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from ..forms.eventForm import EventForm
from ..forms.taskForm import TaskChecklist
from ..models import Event
from ..models import Task
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.utils import timezone


def event_checklist(request, event_id):
    if request.user.is_superuser:
        event = get_object_or_404(Event, id=event_id)
    else:
        event = get_object_or_404(Event, id=event_id, user=request.user)
    TaskFormSet = modelformset_factory(Task, form=TaskChecklist, extra=0)
    queryset = Task.objects.filter(event=event)

    if request.method == 'POST':
        formset = TaskFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('home')
        else:
            print(formset.errors)
    else:
        formset = TaskFormSet(queryset=queryset)

    return render(request, "event_checklist.html", {
        'formset': formset,
        'event': event
    })


def create_event(request):
    if request.method == 'GET':
        return render(request, 'create_event.html', {
            'formForEvents': EventForm
        })
    else:
        try:
            form = EventForm(request.POST)
            # el commit=False es para que aún no lo guarde en la BD
            newEvent = form.save(commit=False)
            newEvent.save()
            return redirect("home")
        except:
            return render(request, "create_event.html", {
                "formForEvents": EventForm,
                'error': 'Por favor, digite valores válidos'
            })


def edit_event(request, event_id):
    if request.method == 'GET':
        if request.user.is_superuser:
            # Aqui se obtiene el objeto y le indicamos que solo queremos el pk = event_id
            event = get_object_or_404(Event, pk=event_id)
            formForEditEvent = EventForm(instance=event)
        else:
            # Si no es el admin, se hace filtro para que no pueda editar las otros eventos
            event = get_object_or_404(Event, pk=event_id, user=request.user)
            formForEditEvent = EventForm(instance=event)
        # El primer eventId,simplem   ente es el nombre de uan variable. El segundo event es el que se obtiene. El que se llama en el html es el que va entre comillas
        return render(request, "edit_event.html", {'eventId': event, 'form': formForEditEvent})
    else:
        try:
            if request.user.is_superuser:
                event = get_object_or_404(Event, pk=event_id)
                # Obtiene los datos del formulario
                form = EventForm(request.POST, instance=event)
            else:
                event = get_object_or_404(
                    Event, pk=event_id, user=request.user)
                form = EventForm(request.POST, instance=event)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, "edit_event.html", {'eventId': event, 'form': formForEditEvent,
                                                       'error': "Error al intentar actualizar, intente de nuevo"})


def complete_event(request, event_id):
    if request.user.is_superuser:
        event = get_object_or_404(Event, pk=event_id)
    else:
        event = get_object_or_404(Event, pk=event_id, user=request.user)
    if request.method == 'POST':
        event.completed = timezone.now()
        event.save()
        return redirect('home')
    
    
def delete_event(request, event_id):
    if request.user.is_superuser:
        event = get_object_or_404(Event, pk=event_id)
    else:
        event = get_object_or_404(Event, pk=event_id, user=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
