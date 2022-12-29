from django.db import models

from student.models.student import Student


class Mobile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return '{}: {}'.format(self.student, self.mobile)