from django.db import models
from students.models import Student
from teachers.models import Teacher


class Attendance(models.Model):

    STATUS_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'date'], name='unique_attendance_per_day')
        ]

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"