from django.urls import path
from . import views

urlpatterns = [
    
    path(
        'create/',
        views.teacher_create,
        name='teacher_create'

        ),

    path(
        'list/',
        views.techaer_list,
        name='teacher_list'
    ),

    path(
        'detail/<int:id>/',
        views.teachers_details,
        name='teachers_details'
    ),

    path(
        'update/<int:id>/',
        views.teacher_update,
        name='teacher_update'
    ),

    path(
        'update/<int:id>/',
        views.teacher_delete,
        name='teacher_delete'
    ),

]
