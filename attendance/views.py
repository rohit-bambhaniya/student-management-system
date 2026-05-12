from django.shortcuts import render
from students.models import Student

def mark_attendance(request):

    students = Student.objects.all()

    context = {

        'students' : students
    }

    return render (request, 'attendance/mark_attendance.html', context)

# Create your views here.
