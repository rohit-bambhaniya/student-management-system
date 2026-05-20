from django.db import models
from accounts.models import User
from classroom.models import Classroom


class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    student_name = models.CharField(
        max_length=255,
        null=True,
        blank=True

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
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):

        return self.user.username