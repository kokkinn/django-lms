# Generated by Django 4.0 on 2022-01-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_remove_teacher_group'),
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='teachers',
            field=models.ManyToManyField(related_name='groups', to='teachers.Teacher'),
        ),
    ]
