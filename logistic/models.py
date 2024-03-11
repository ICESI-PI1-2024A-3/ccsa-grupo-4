from django.db import models
# In here, we create the clases that later on, they turn into sql tables
# Create your models here.

class Event(models.Model):
    registerDate = models.DateField()
    name = models.CharField(max_length = 200)
    executionDate = models.DateField()
    place = models.CharField(max_length = 200)
    manager = models.CharField(max_length = 200)
    progress = models.IntegerField() #en revision
    finishDate = models.DateField()
    #bitacora = models.#####() #en revision

#Single Table Inheritance:
class User(models.Model):
    name = models.CharField(max_length = 255)
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    rol = models.CharField(max_length = 255) #with this, we don't need another table called rol

class Inquiry(models.Model):
    id = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length = 200)
    description = models.TextField()
    feedback = models.TextField()
