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
