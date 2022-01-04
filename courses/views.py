from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from students.models import Students
from .forms import CoursesFilter, CourseCreateForm, CourseUpdateForm

from .models import Course


def get_courses(request):
    courses = Course.objects.all()
    filter_courses = CoursesFilter(data=request.GET, queryset=courses)
    return render(
        request=request,
        template_name='courses/list.html',
        context={"filter_courses": filter_courses}
    )


def create_course(request):
    if request.method == 'GET':
        form = CourseCreateForm()
    elif request.method == 'POST':
        form = CourseCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )


def update_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'GET':
        form = CourseUpdateForm(instance=course)
    elif request.method == 'POST':
        form = CourseUpdateForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(
        request=request,
        template_name='courses/update.html',
        context={'form': form}
    )


def delete_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == "POST":
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {"coure": course})
