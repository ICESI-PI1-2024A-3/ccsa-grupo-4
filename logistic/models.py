from django.db import models


class User(models.Model):

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):

    registerDate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
