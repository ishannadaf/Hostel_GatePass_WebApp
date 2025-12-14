from django.urls import path
from .views import add_student, student_list, student_edit, student_delete

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('', student_list, name='student_list'),
    path('edit/<int:id>/', student_edit, name='student_edit'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
]
