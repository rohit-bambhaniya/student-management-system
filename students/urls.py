from django.urls import path
from . import views

urlpatterns = [

    path('create/',
        views.student_create,
        name='student_create'
    ),

    path('list/', 
        views.student_list,
        name='student_list'
    ),

    path('update/<int:id>/',
        views.student_update,
        name='student_update'
    ),

    path(
        'delete/<int:id>/',
        views.student_delete,
        name='student_delete'
    ),

    path(
        'detail/<int:id>/',
        views.student_detail,
        name='student_detail'
    ),

]