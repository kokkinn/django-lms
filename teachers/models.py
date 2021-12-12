from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()
    specialization = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.age} {self.specialization}"
