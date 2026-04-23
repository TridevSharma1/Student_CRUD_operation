from django.urls import path
from . import views

urlpatterns = [
    path('students', views.student_list, name='student_list'),
    path('add/', views.add_student),
    # path('delete/<int:id>/', views.delete_student),
    # path('edit/<int:id>/', views.edit_student),
]