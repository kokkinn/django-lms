from django.db import models


class Groups(models.Model):
    course = models.IntegerField()
    letter = models.CharField(max_length=1)
    fullname = models.CharField(max_length=2)
    number_of_students = models.IntegerField()
    name_of_teacher = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course} {self.letter} {self.fullname} {self.number_of_students} {self.name_of_teacher}"


