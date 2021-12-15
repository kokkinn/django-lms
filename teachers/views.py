from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm
from teachers.models import Teacher
from teachers.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


@use_args({'first_name': fields.Str(required=False),
           'second_name': fields.Str(required=False),
           'age': fields.Int(required=False),
           'specialization': fields.Str(required=False)}, location='query')
def get_teachers(reqest, args):
    teachers = Teacher.objects.all()
    for key, value in args.items():
        if value:
            teachers = teachers.filter(**{key: value})
    html_form = """
                    <form method="get">
                        <label for="fname">First name:</label>
                        <input type="text" id="fname" name="first_name"></br></br>
                        <label for="lname">Last name:</label>
                        <input type="text" id="lname" name="second_name"></br></br>
                        <label for="age">Age:</label>
                        <input type="number" name="age"></br></br>
                        <label for="spec">Specialization:</label>
                        <input type="text" id="spec" name="specialization"></br></br>
                        <input type="submit" value="Submit">
                    </form>
                """
    teachers = format_records(teachers)
    resonse = html_form + teachers
    return HttpResponse(resonse)


@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers')

    html_form = f"""
                <form method="post">
                    {form.as_p()}
                    <input type="submit" value="Submit">
                </form>
            """
    return HttpResponse(html_form)
