from django.db import models
from accounts.models import User

class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    subject = models.CharField(
        max_length=100
    )
    
    phone = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.user.username

# Create your models here.
