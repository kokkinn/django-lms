from django.http import HttpResponse
from .models import Students


def generate_students(request):
    return HttpResponse(Students.generate_students(request))
