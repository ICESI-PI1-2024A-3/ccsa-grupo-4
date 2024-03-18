from django.db import models
from django.contrib.auth.models import User



class User(models.Model):

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    registerDate = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 200)
    executionDate = models.DateField()
    place = models.CharField(max_length = 200)
    progress = models.IntegerField() #en revision
    finishDate = models.DateTimeField(null= True)
    important = models.BooleanField(default = False)
    completed =models.DateTimeField(null = True, blank = True)
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
  