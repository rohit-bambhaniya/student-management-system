from django.db import models
from teachers.models import Teacher
from students.models import Student

class Attendance(models.Model):

    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent')
    )

    student = models.ForeignKey(
        Student,
        on_delete = models.CASCADE
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete = models.CASCADE
    )

    date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices = STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.student} - {self.status}"
# Create your models here.
