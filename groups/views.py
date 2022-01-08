from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from groups.forms import GroupCreateForm, GroupsFilter, GroupUpdateForm
from groups.models import Groups
from students.models import Students


class GroupListView(ListView):
    model = Groups
    template_name = "groups/list.html"

    def get_queryset(self):
        filter_groups = GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related("headman", "course"))

        return filter_groups


class GroupCreateView(CreateView):
    model = Groups
    form_class = GroupCreateForm
    success_url = reverse_lazy("groups:list")
    template_name = 'groups/create.html'


class GroupDeleteView(DeleteView):
    model = Groups
    success_url = reverse_lazy("groups:list")


class GroupUpdateView(UpdateView):
    model = Groups
    form_class = GroupUpdateForm
    success_url = reverse_lazy("groups:list")
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = self.get_object().students.prefetch_related("headman_group")

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial["headman_field"] = self.object.headman.id
        except AttributeError as ex:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = form.cleaned_data["headman_field"]
        if pk:
            form.instance.headman = Students.objects.get(id=form.cleaned_data["headman_field"])
        form.instance.save()
        return response

# def group_create(request):
#     if request.method == 'GET':
#         form = GroupCreateForm()
#     elif request.method == 'POST':
#         form = GroupCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     return render(
#         request=request,
#         template_name='groups/create.html',
#         context={'form': form}
#     )

# def update_group(request, pk):
#     group = Groups.objects.get(id=pk)
#     if request.method == 'GET':
#         form = GroupCreateForm(instance=group)
#     elif request.method == 'POST':
#         form = GroupCreateForm(data=request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(
#         request=request,
#         template_name='groups/update.html',
#         context={'form': form,
#                  "students": group.students.prefetch_related("headman_group")}
#     )

# def delete_group(request, pk):
#     group = get_object_or_404(Groups, id=pk)
#     if request.method == "POST":
#         group.delete()
#         return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(request, 'groups/groups_confirm_delete.html', {"group": group})

# def get_groups(request):
#     groups = Groups.objects.all()
#     filter_groups = GroupsFilter(data=request.GET, queryset=groups)
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={"filter_groups": filter_groups}
#     )
