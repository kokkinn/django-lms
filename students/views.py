from django.http import HttpResponse

from students.models import Students

from webargs import fields
from webargs.djangoparser import use_args

from .utils import format_records


# def generate_students(request):
#     return HttpResponse(Students.generate_students(request))

@use_args({'first_name': fields.Str(required=False),
           'second_name': fields.Str(required=False),
           'age': fields.Str(required=False)
           }, location='query')
def get_students(request, args):
    students = Students.objects.all()
    for key, value in args.items():
        if value:
            students = students.filter(**{key: value})
    html_form = """
                <form method="get">
                    <label for="fname">First name:</label>
                    <input type="text" id="fname" name="first_name"></br></br>
                    <label for="lname">Last name:</label>
                    <input type="text" id="lname" name="second_name"></br></br>
                    <label for="age">Age:</label>
                    <input type="number" name="age"></br></br>
                    <input type="submit" value="Submit">
                </form>
            """
    studentz = format_records(students)
    response = html_form + studentz
    return HttpResponse(response)
