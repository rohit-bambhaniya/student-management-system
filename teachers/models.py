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

    qualifications = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    experience = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    
    phone = models.CharField(
        max_length=15
    )

    address = models.TextField(
        blank=True,
        null = True
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    joining_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

# Create your models here.
