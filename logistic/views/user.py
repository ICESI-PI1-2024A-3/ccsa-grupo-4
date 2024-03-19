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
from ..forms import EventForm
from ..forms import TaskForm
from ..forms import TaskChecklist
from ..models import Event
from ..models import Task
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.utils import timezone
from ..models import User

def home(request):
    if request.user.is_superuser:  # Si es el admin, lista todas las tareas
        events = Event.objects.all()
    else:  # si no es el admin, solo lista las tareas asociadas a el/ella
        events = Event.objects.filter(user=request.user)
    return render(request, 'home.html', {'Eventos': events})