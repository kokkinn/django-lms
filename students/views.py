from copy import copy

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.views import UpdateBaseView
from students.models import Students

from .forms import StudentCreateForm, StudentUpdateForm
from .forms import StudentsFilter


class StudentsListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Students
    template_name = "students/list.html"

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related("group", "headman_group"))

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = self.get_filter().form
    #
    #     params = self.request.GET
    #     if 'page' in params:
    #         params = copy(params)
    #         del params['page']
    #     context['get_params'] = '&' + params.urlencode() if params else ''  # convert dict to str

        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy("students:list")
    template_name = 'students/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f"Student was successfully created")
        return result


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f"Student {self.get_object()} was successfully updated")
        return result


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Students
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        student = self.get_object()
        result = super().form_valid(form)
        messages.success(self.request, f"Student {student} was successfully deleted")
        return result

# def get_students(request):
#     students = Students.objects.all().select_related("group", "headman_group")
#     filter_students = StudentsFilter(data=request.GET, queryset=students)
#     return render(
#         request=request,
#         template_name='students/list.html',
#         context={"filter_students": filter_students}
#     )
#
#
# def create_student(request):
#     if request.method == 'GET':
#         form = StudentCreateForm()
#     elif request.method == 'POST':
#         form = StudentCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#     return render(
#         request=request,
#         template_name='students/create.html',
#         context={'form': form}
#     )
#
#
# def update_student(request, pk):
#     student = Students.objects.get(id=pk)
#     if request.method == 'GET':
#         form = StudentCreateForm(instance=student)
#     elif request.method == 'POST':
#         form = StudentCreateForm(data=request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#     return render(
#         request=request,
#         template_name='students/update.html',
#         context={'form': form}
#     )
#
#
#
# @login_required
# def delete_student(request, pk):
#     student = get_object_or_404(Students, id=pk)
#     if request.method == "POST":
#         student.delete()
#         return HttpResponseRedirect(reverse('students:list'))
#
#     return render(request, 'students/groups_confirm_delete.html', {"student": student})
# #
# #
# # "Ниже реализация Class Based View вручную"
#
#
# class UpdateStudentView(UpdateBaseView):
#     model = Students
#     form_class = StudentUpdateForm
#     success_url = 'students:list'
#     template_name = 'students/update.html'
