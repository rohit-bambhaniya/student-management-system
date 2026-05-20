from django.db import models

from django.db import models
from teachers.models import Teacher


class Classroom(models.Model):

    class_name = models.CharField(
        max_length=50,
        unique=True
    )

    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='classrooms'
    )

    section = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    room_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        if self.section:
            return f"{self.class_name} - {self.section}"
        return self.class_name

# Create your models here.
