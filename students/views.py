from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from students.models import Students

from webargs import fields
from webargs.djangoparser import use_args

from .forms import StudentCreateForm
from .forms import StudentsFilter


@use_args({'first_name': fields.Str(required=False),
           'second_name': fields.Str(required=False),
           'age': fields.Str(required=False)
           }, location='query')
def get_students(request, args):
    students = Students.objects.all()
    for key, value in args.items():
        if value:
            students = students.filter(**{key: value})

    filter_students = StudentsFilter(data=request.GET, queryset=students)
    return render(
        request=request,
        template_name='students/list.html',
        context={'students': students, "filter_students":filter_students}
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
