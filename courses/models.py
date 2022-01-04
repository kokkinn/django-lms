import datetime

from django.db import models

from groups.models import Groups


class Course(models.Model):

    course_name = models.CharField(max_length=30)
    start_date = models.DateField(default=datetime.date.today)
    group = models.OneToOneField(
        Groups,
        on_delete=models.CASCADE,
        null=True,
        related_name='course'
    )

    def __str__(self):
        return f'{self.course_name}'

    # def save(self, *args, **kwargs):
    #     self.start_date = self.group.start_date
    #     super().save(*args, **kwargs)
