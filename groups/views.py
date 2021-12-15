from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Groups
from groups.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
            'name': fields.Str(required=False),
            # 'sta': fields.Str(required=False),
            # 'number_of_students': fields.Int(required=False),
        }, location='query')
def get_groups(request, args):
    groups = Groups.objects.all()
    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})
    html_form = """
                    <form method="get">
                    <label for="name">Name of group:</label>
                    <input type="text" id="name" name="name"></br></br>
                    <input type="submit" value="Submit"></form>             
                     """
    groups = format_records(groups)
    response = html_form + groups
    return HttpResponse(response)


@csrf_exempt
def group_create(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')

    html_form = f"""
                <form method="post">
                    {form.as_p()}
                    <input type="submit" value="Submit">
                </form>
            """
    return HttpResponse(html_form)
