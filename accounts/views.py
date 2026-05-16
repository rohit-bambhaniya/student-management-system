from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from students.models import Student


# Login View
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Role Based Redirect
            if user.is_admin():
                return redirect('admin_dashboard')

            elif user.is_teacher():
                return redirect('teacher_dashboard')

            elif user.is_student():
                return redirect('student_dashboard')

    return render(request, 'accounts/login.html')


# Logout View
def logout_view(request):

    logout(request)

    return redirect('login')


# Admin Dashboard
@login_required
def admin_dashboard(request):

    return render(
        request,
        'accounts/admin_dashboard.html'
    )


# Teacher Dashboard
@login_required
def teacher_dashboard(request):

    return render(
        request,
        'accounts/teacher_dashboard.html'
    )


# Student Dashboard
@login_required
def student_dashboard(request):

    student = Student.objects.get(
        user=request.user
    )

    context = {

        'student': student
    }

    return render(
        request,
        'accounts/student_dashboard.html',
        context
    )