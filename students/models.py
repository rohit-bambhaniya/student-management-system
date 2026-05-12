from django.db import models
from accounts.models import User

class Student(models.Model):

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    roll_num = models.CharField(
        max_length=20
    )
    student_class = models.CharField(
        max_length=50
    )
    phone = models.CharField(
        max_length=15
    )

class Meta:
    unique_together = ('student', 'date')

    def __str__(self):
        return self.user.username



# Create your models here.
