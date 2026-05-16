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

    address = models.TextField(
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.user.username