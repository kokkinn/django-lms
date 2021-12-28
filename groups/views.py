from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupsFilter
from groups.models import Groups


def get_groups(request):
    groups = Groups.objects.all()
    filter_groups = GroupsFilter(data=request.GET, queryset=groups)
    return render(
        request=request,
        template_name='groups/list.html',
        context={"filter_groups": filter_groups}
    )


def group_create(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = Groups.objects.get(id=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form, "group": group}
    )


def delete_group(request, pk):
    group = get_object_or_404(Groups, id=pk)
    if request.method == "POST":
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {"group": group})
