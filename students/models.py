from django.db import models
from faker import Faker


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()

    @staticmethod
    def generate_students(request):
        fake = Faker()
        countt = 10

        if 'count' in request.GET:
            if request.GET['count'].isdigit():
                countt = int(request.GET['count'])

        for _ in range(countt):
            st = Students(first_name=fake.first_name(),
                          second_name=fake.last_name(),
                          age=fake.pyint(12, 100))
            st.save()

        return f'{countt} students were generated'
