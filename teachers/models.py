from django.db import models

class Teacher(models.Model):
    username = models.TextField(max_length=250)
    password = models.TextField(max_length=50)

    def __str__(self):
        return models.username

# Create your models here.
