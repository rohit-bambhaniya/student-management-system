from django.shortcuts import render, redirect
from students.models import Student
from .models import Attendance
from datetime import date
from teachers.models import Teacher


def mark_attendance(request):

    print("LOGIN USER:", request.user.username)
    print("LOGIN USER ID:", request.user.id)

    teacher = Teacher.objects.filter(user=request.user).first()

    teacher = Teacher.objects.filter(user=request.user).first()

    if not teacher:
       teacher = Teacher.objects.first()
    
    students = Student.objects.all()

    if request.method == "POST":

        for student in students:
            status = request.POST.get(f'student_{student.id}')

            if status in ['P', 'A']:

                Attendance.objects.update_or_create(
                    student=student,
                    date=date.today(),
                    defaults={
                        'teacher': teacher,
                        'status': status
                    }
                )

        return redirect('attendance_report')

    return render(request, 'attendance/mark_attendance.html', {
        'students': students
    })


def attendance_report(request):

    teacher = Teacher.objects.filter(user=request.user).first()

    if not teacher:
       teacher = Teacher.objects.first()

    records = Attendance.objects.filter(teacher=teacher).order_by('-date')

    return render(request, 'attendance/report.html', {
        'records': records
    })