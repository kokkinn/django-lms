from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from students.models import Students

from .forms import StudentCreateForm
from .forms import StudentsFilter


def get_students(request):
    students = Students.objects.all()
    filter_students = StudentsFilter(data=request.GET, queryset=students)
    return render(
        request=request,
        template_name='students/list.html',
        context={"filter_students": filter_students}
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


def update_student(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form}
    )


def delete_student(request, pk):
    student = get_object_or_404(Students, id=pk)
    if request.method == "POST":
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {"student": student})
