from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Login View
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            # Role-based redirect
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