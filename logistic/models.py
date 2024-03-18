from django.db import models
from django.contrib.auth.models import User
# In here, we create the clases that later on, they turn into sql tables
# Create your models here.

class Event(models.Model):
    registerDate = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 200)
    executionDate = models.DateField()
    place = models.CharField(max_length = 200)
    progress = models.IntegerField() #en revision
    finishDate = models.DateTimeField(null= True)
    important = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)#Esto me relaciona esta tabla con la tabla de usuarios. Si quiero que cuando se elimine el usuario se elimine todo entonces uso (User, on_delete = models.CASCADE)
    #bitacora = models.#####() #en revision
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 500)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null = True)
    done = models.BooleanField(default = False)
    

class Inquiry(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length = 200)#Es para saber a que evento está relacionado
    description = models.TextField()
    feedback = models.TextField()
    #event = models.ForeignKey(Event, on_delete = models.CASCADE)#Preguntar esto, se supone que es para que aparezca un id que haga referencia al evento que está relacionado
