from django.db import models

from student.models.student import Student


class Course(models.Model):
    name = models.CharField(max_length=20)
    duration = models.FloatField()
    is_available = models.BooleanField(default=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
