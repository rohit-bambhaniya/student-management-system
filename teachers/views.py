from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeacherForm
from .models import Teacher


def teacher_create(request):

        
    if request.method == "POST":

        form = TeacherForm(request.POST)

        if form.is_valid():

            print("VALID FORM")
            form.save()

            return redirect('admin_dashboard')
        
        else:

            print("ERRORS:", form.errors)
    
    else:

        form = TeacherForm()

    return render(request,'teachers/teacher_create.html',{'form':form})

def techaer_list(request):

    teachers = Teacher.objects.all()

    context = {

        'teachers':teachers
    }

    return render(request, 'teachers/teacher_list.html',context)


def teachers_details(request, id):

    teacher = get_object_or_404(
        Teacher,
        id=id
    )

    context = {

        'teacher':teacher
    }

    return render(request,'teachers/teacher_detail.html',context)

def teacher_update(request, id):

    teacher = get_object_or_404(

        Teacher,
        id=id
    )

    if request.method == 'POST':

        form = TeacherForm(
            request.POST,
            instance=teacher
        )

        if form.is_valid():

            form.save()

            return redirect('teacher_list')
        
    else:

        form = TeacherForm(instance=teacher)

    context = {

        'form': form 
    }

    return render(
        request,
        'teachers/teacher_form.html',
        context
    )
    
def teacher_delete(request, id):

    teacher = get_object_or_404(
        Teacher,
        id=id
    )

    if request.method == 'POST':

        teacher.delete()

        return redirect('teacher_list')
    
    context = {

        'teacher' : teacher
    }

    return render(
        request, 
        'teachers/teacher_delete.html',
        context
    )






# Create your views here.
