from django.db import IntegrityError
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import EventForm
from .forms import TaskForm
from .forms import TaskChecklist
from .models import Event
from .models import Task
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import User


def search_users(request):

    name_query = request.GET.get('name', None)
    id_query = request.GET.get('id', None)

    users = []

    if name_query:

        users = User.objects.filter(name__icontains=name_query)

    elif id_query:

        users = User.objects.filter(id_number=id_query)

    return render(request, 'users/users_search.html', {'users': users})


def home(request):
    if request.user.is_superuser:  # Si es el admin, lista todas las tareas
        events = Event.objects.all()
    else:  # si no es el admin, solo lista las tareas asociadas a el/ella
        events = Event.objects.filter(user=request.user)
    return render(request, 'home.html', {'Eventos': events})


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


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists',
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match',
        })


def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')


def admin(request):
    return redirect(admin.site.urls)


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
