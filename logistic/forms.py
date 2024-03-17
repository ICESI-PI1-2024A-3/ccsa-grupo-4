from django.forms import ModelForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import Event
from .models import Task



class EventForm(ModelForm):
    user = ModelChoiceField(queryset=User.objects.all()) #Esto agrega un campo de seleccon para el usuario, de lo contrario arroja error de validacion

    class Meta:
        model = Event
        fields = ["name", "executionDate", "place", "progress", "finishDate", "important", "user"]

class TaskForm(ModelForm):
    event = ModelChoiceField(queryset=Event.objects.all())

    class Meta:
        model = Task
        fields = ["name", "event", "done"]
