from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Groups
from groups.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


@use_args({'name': fields.Str(required=False)}, location='query')
def get_groups(request, args):
    groups = Groups.objects.all()
    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})
    return render(
        request=request,
        template_name='groups/list.html',
        context={'groups': groups}
    )


def group_create(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')
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
            return HttpResponseRedirect('/groups')

    # html_form = f"""
    #             <form method="post">
    #                 {form.as_p()}
    #                 <input type="submit" value="Update">
    #             </form>
    #         """
    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form}
    )
