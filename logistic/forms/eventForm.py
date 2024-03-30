from django.forms import ModelForm
from django.forms import DateTimeInput
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from ..models import Event


class EventForm(ModelForm):
    user = ModelChoiceField(queryset=User.objects.all(), label="Usuario") #Esto agrega un campo de seleccon para el usuario, de lo contrario arroja error de validacion

    class Meta:
        model = Event
        fields = ["name", "executionDate", "place", "progress", "finishDate", "important", "user"]
        widgets = {
            'executionDate': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'finishDate': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        labels = {
            'name': 'Nombre',
            'executionDate': 'Fecha de Ejecución',
            'place': 'Lugar',
            'progress': 'Progreso',
            'finishDate': 'Fecha de Finalización',
            'important': 'Importante',
            'user': 'Usuario'
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['executionDate'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['finishDate'].input_formats = ('%Y-%m-%dT%H:%M',)

