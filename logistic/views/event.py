from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from ..forms.taskForm import TaskChecklist
from ..models import Event
from ..models import Task
from django.forms import modelformset_factory
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from ..forms.eventForm import EventForm
from django.conf import settings
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
import json



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

            subject = 'Actualización de lista de tareas'
            message = f'Se ha actualizado la lista de tareas para el evento "{event.name}".'
            from_email = 'your@example.com'
            recipient_list = ['recipient@example.com']

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                print(f"Error al enviar correo electrónico: {e}")

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
        users_event = User.objects.all(
        ) if request.user.is_superuser else User.objects.filter(id=request.user.id)
        form = EventForm()
        form.fields['user'].queryset = users_event
        return render(request, 'create_event.html', {'formForEvents': form})
    elif request.method == 'POST':
        try:
            user_events = User.objects.all(
            ) if request.user.is_superuser else User.objects.filter(id=request.user.id)
            form = EventForm(request.POST)
            form.fields['user'].queryset = user_events
            if form.is_valid():
                new_event = form.save(commit=False)
                if not request.user.is_superuser:
                    new_event.user = request.user
                new_event.save()

                subject = 'Nuevo evento creado'
                message = f'Se ha creado un nuevo evento: {new_event.name}'
                from_email = 'your@example.com'
                recipient_list = ['recipient@example.com']

                send_mail(subject, message, from_email, recipient_list)

                return redirect("home")
            else:
                return render(request, 'create_event.html', {'formForEvents': form})
        except Exception as e:
            print(f"Error al enviar correo electrónico: {e}")
            return render(request, "create_event.html", {
                "formForEvents": EventForm(),
                'error': 'Por favor, digite valores válidos'
            })



def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'GET':
        user_events = User.objects.all(
        ) if request.user.is_superuser else User.objects.filter(id=request.user.id)
        if request.user.is_superuser or event.user == request.user:
            form = EventForm(instance=event)
            form.fields['user'].queryset = user_events
            return render(request, "edit_event.html", {'eventId': event, 'form': form})
        else:
            messages.error(
                request, "No tiene permiso para editar este evento.")
            return redirect('home')
    elif request.method == 'POST':
        try:
            user_events = User.objects.all(
            ) if request.user.is_superuser else User.objects.filter(id=request.user.id)
            form = EventForm(request.POST, instance=event)
            form.fields['user'].queryset = user_events
            if request.user.is_superuser or event.user == request.user:
                if form.is_valid():
                    updated_event = form.save()
                    subject = 'Evento Actualizado'
                    message = f"Se ha actualizado el evento: {updated_event.name}"
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [request.user.email]
                    send_mail(subject, message, from_email, to_email)
                    return redirect('home')
                else:
                    return render(request, 'edit_event.html', {'eventId': event, 'form': form})
            else:
                messages.error(
                    request, "No tiene permiso para editar este evento.")
                return redirect('home')
        except ValueError:
            messages.error(
                request, "Error al intentar actualizar, intente de nuevo")
            return render(request, "edit_event.html", {'eventId': event, 'form': form})



def complete_event(request, event_id):
    if request.user.is_superuser:
        event = get_object_or_404(Event, pk=event_id)
    else:
        event = get_object_or_404(Event, pk=event_id, user=request.user)

    if request.method == 'POST':
        event.completed = timezone.now()
        event.save()

        subject = 'Evento completado'
        message = f'El evento "{event.name}" ha sido completado.'
        from_email = 'your@example.com'
        recipient_list = ['recipient@example.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print(f"Error al enviar correo electrónico: {e}")

        return redirect('home')



def delete_event(request, event_id):
    if request.user.is_superuser:
        event = get_object_or_404(Event, pk=event_id)
    else:
        event = get_object_or_404(Event, pk=event_id, user=request.user)
    
    if request.method == 'POST':
        event.delete()
        return redirect('home')


def events_calendar(request):
    if request.user.is_superuser:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(user=request.user)

    local_tz = local_tz = timezone.get_current_timezone()

    events_for_calendar = [
        {
            'title': event.name,
            'start': event.executionDate.astimezone(local_tz).isoformat() if event.executionDate else None,
            'end': event.finishDate.astimezone(local_tz).isoformat() if event.finishDate else None,
            'color': 'red' if event.important else 'blue',
            'url': f"/event/checklist/{event.id}",
            'username': event.user.username if event.user else 'Sin usuario',
        }
        for event in events
    ]

    context = {
        'events_json': json.dumps(events_for_calendar),
    }

    return render(request, 'events_calendar.html', context)
