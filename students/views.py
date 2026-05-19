from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student


def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

def student_list(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'students/student_list.html',context)

def student_update(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:

        form = StudentForm(
            instance=student
        )

    context = {

        'form': form
    }

    return render(
        request,
        'students/student_form.html',
        context
    )

def student_delete(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == 'POST':

        student.delete()

        return redirect('student_list')

    context = {

        'student': student

    }

    return render(
        request,
        'students/student_delete.html',
        context
    )
def student_detail(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    context = {

        'student': student

    }

    return render(
        request,
        'students/student_detail.html',
        context
    )