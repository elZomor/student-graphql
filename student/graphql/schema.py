from _ast import Delete

import graphene
import graphql_jwt
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations as graph_auth
from graphql_jwt.decorators import login_required

from student.graphql.fields import StudentClass, CourseClass, MobileClass
from student.graphql.mutations import CreateCourse, CreateStudent, AssignCoursesToStudent, AssignStudentsToCourse, \
    DeleteStudent
from student.models import Student, Course, Mobile


class Query(UserQuery, MeQuery, graphene.ObjectType):
    students = graphene.List(StudentClass, course_name=graphene.String())
    student = graphene.Field(StudentClass, id=graphene.ID(), name=graphene.String(), mobile=graphene.String())
    mobiles = graphene.List(MobileClass, student_name=graphene.String())
    courses = graphene.List(CourseClass, is_available=graphene.Boolean())
    course = graphene.Field(CourseClass, id=graphene.ID())

    def resolve_students(info, course_name=None, *args, **kwargs):
        if course_name:
            course = Course.objects.filter(name=course_name).last()
            return course.students.all() if course else []
        return Student.objects.all()

    @login_required
    def resolve_student(self, info, student_id=None, name=None, mobile=None, *args, **kwargs):
        if student_id:
            return Student.objects.get(id=student_id)
        if name:
            return Student.objects.filter(name=name).last()
        if mobile:
            mobile = Mobile.objects.filter(mobile=mobile).last()
            return mobile.student if mobile else []
        return None

    def resolve_mobiles(self, info, student_name=None, *args, **kwargs):
        if student_name:
            return Mobile.objects.filter(student=Student.objects.filter(name=student_name).last())
        return Mobile.objects.all()

    def resolve_courses(self, info, is_available=None, *args, **kwargs):
        if is_available:
            return Course.objects.filter(is_available=is_available)
        return Course.objects.all()

    def resolve_course(self, info, course_id=None, name=None, *args, **kwargs):
        if name:
            return Course.objects.filter(name=name).last()
        return Course.objects.get(id=course_id)


class Mutation(graphene.ObjectType):
    """
        JWT and Auth APIs are almost the same, you can use whatever suits you
    """
    # JWT Token APIs
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    # Auth Token APIs
    register = graph_auth.Register.Field()

    create_course = CreateCourse.Field()
    create_student = CreateStudent.Field()
    assign_courses = AssignCoursesToStudent.Field()
    assign_students = AssignStudentsToCourse.Field()
    delete_student = DeleteStudent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
