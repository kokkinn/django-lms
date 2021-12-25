from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm, GroupsFilter
from groups.models import Groups
from groups.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


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
        context={'form': form}
    )


def delete_group(request, pk):
    group = get_object_or_404(Groups, id=pk)
    if request.method == "POST":
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {"group": group})
