from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm, TeachersFilter
from teachers.models import Teacher
from teachers.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


def get_teachers(request):
    teacher = Teacher.objects.all()
    filter_teachers = TeachersFilter(data=request.GET, queryset=teacher)
    return render(
        request=request,
        template_name='teachers/list.html',
        context={'filter_teachers': filter_teachers}
    )


def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


def update_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == "POST":
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {"teacher": teacher})
