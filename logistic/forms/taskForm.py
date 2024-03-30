from django.forms import ModelForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from ..models import Task
from ..models import Event

class TaskForm(ModelForm):
    event = ModelChoiceField(queryset=Event.objects.all(), label="Evento")

    class Meta:
        model = Task
        fields = ["name", "event", "done"]
        
        labels = {
            'name': 'Nombre',
            'event': 'Evento',
            'done': 'Hecho' ,      
        }
        

class TaskChecklist(ModelForm):
    class Meta:
        model = Task
        fields = ["done"] 
    
        labels = {
            
            'done': 'Hecho',
        }


