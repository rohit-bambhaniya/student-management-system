from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import Student
from teachers.models import Teacher
from accounts.models import User


# Admin Dashboard
@login_required
def admin_dashboard(request):

    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_admins = User.objects.filter(role="admin").count()

    recent_students = Student.objects.order_by('-id')[:5]
    recent_teachers = Teacher.objects.order_by('-id')[:5]

    return render(request, 'core/admin_dashboard.html', {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_admins': total_admins,
        'recent_students': recent_students,
        'recent_teachers': recent_teachers,
    })


# Teacher Dashboard
@login_required
def teacher_dashboard(request):

    teacher = Teacher.objects.get(user=request.user)

    return render(request, 'core/teacher_dashboard.html', {
        'teacher': teacher
    })


# Student Dashboard
@login_required
def student_dashboard(request):

    student = Student.objects.get(user=request.user)

    return render(request, 'core/student_dashboard.html', {
        'student': student
    })