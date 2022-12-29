from enum import Enum

from django.db import models


class Grades(Enum):
    GRADE_ONE = 1
    GRADE_TWO = 2
    GRADE_THREE = 3

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField(choices=Grades.choices())
    picture = models.FileField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name
