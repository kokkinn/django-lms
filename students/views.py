from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView

from core.views import UpdateBaseView
from students.models import Students

from .forms import StudentCreateForm, StudentUpdateForm
from .forms import StudentsFilter


def get_students(request):
    students = Students.objects.all().select_related("group", "headman_group")
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

    return render(request, 'students/groups_confirm_delete.html', {"student": student})


"Ниже реализация Class Based View вручную"


class UpdateStudentView(UpdateBaseView):
    model = Students
    form_class = StudentUpdateForm
    success_url = 'students:list'
    template_name = 'students/update.html'


class StudentUpdateView(UpdateView):
    model = Students
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentsListView(ListView):
    model = Students
    template_name = "students/list.html"

    def get_queryset(self):
        filter_students = StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related("group", "headman_group"))

        return filter_students


class StudentDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
