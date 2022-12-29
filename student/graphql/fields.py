import graphene
from graphene import InputObjectType
from graphene_django import DjangoObjectType

from student.models import Student, Course, Mobile


class CourseClass(DjangoObjectType):
    class Meta:
        model = Course


class StudentClass(DjangoObjectType):
    courses = graphene.List(CourseClass)

    class Meta:
        model = Student

    def resolve_courses(self, *args, **kwargs):
        return self.course_set.all()


class MobileClass(DjangoObjectType):
    class Meta:
        model = Mobile


class CourseListClass(InputObjectType):
    course = graphene.Field(CourseClass)


