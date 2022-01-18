from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from groups.models import Groups
from teachers.forms import TeacherCreateForm, TeachersFilter, TeacherUpdateForm
from teachers.models import Teacher


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = "teachers/list.html"

    def get_queryset(self):
        filter_teachers = TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all())
        # .select_related("group", "headman_group"))

        return filter_teachers


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy("teachers:list")
    template_name = 'teachers/create.html'

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     pk = form.cleaned_data["group_field"]
    #     if pk:
    #         form.instance.groups = Groups.objects.filter(id=form.cleaned_data["headman_field"])
    #     form.instance.save()
    #     return response

# def get_teachers(request):
#     teacher = Teacher.objects.all()
#     filter_teachers = TeachersFilter(data=request.GET, queryset=teacher)
#     return render(
#         request=request,
#         template_name='teachers/list.html',
#         context={'filter_teachers': filter_teachers}
#     )
#
#
# def create_teacher(request):
#     if request.method == 'GET':
#         form = TeacherCreateForm()
#     elif request.method == 'POST':
#         form = TeacherCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#     return render(
#         request=request,
#         template_name='teachers/create.html',
#         context={'form': form}
#     )
#
#
# def update_teacher(request, pk):
#     teacher = Teacher.objects.get(id=pk)
#     if request.method == 'GET':
#         form = TeacherCreateForm(instance=teacher)
#     elif request.method == 'POST':
#         form = TeacherCreateForm(data=request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#     return render(
#         request=request,
#         template_name='teachers/update.html',
#         context={'form': form}
#     )
#
#
# def delete_teacher(request, pk):
#     teacher = get_object_or_404(Teacher, id=pk)
#     if request.method == "POST":
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teachers:list'))
#
#     return render(request, 'teachers/groups_confirm_delete.html', {"teacher": teacher})
