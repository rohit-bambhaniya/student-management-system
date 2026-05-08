from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (TEACHER, 'teacher'),
        (STUDENT, 'student'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT
    )

    def is_admin(self):
        return self.role == self.ADMIN

    def is_teacher(self):
        return self.role == self.TEACHER

    def is_student(self):
        return self.role == self.STUDENT

    def __str__(self):
        return f"{self.username} ({self.role})"