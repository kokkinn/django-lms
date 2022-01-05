from django.urls import path

from .views import create_student, delete_student, StudentUpdateView, StudentsListView

app_name = 'students'

urlpatterns = [
    path('', StudentsListView.as_view(), name='list'),
    path('create/', create_student, name="create"),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', delete_student, name="delete"),

]
