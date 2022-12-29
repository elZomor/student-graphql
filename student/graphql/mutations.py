import graphene
from graphene import ID
from graphene_file_upload.scalars import Upload
from graphql_auth.decorators import verification_required
from graphql_jwt.decorators import login_required, superuser_required

from student.graphql.fields import CourseClass, StudentClass, MobileClass, CourseListClass
from student.models import Course, Mobile
from student.models.student import Student, Grades


class GenericField(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()

    def __init__(self, error=None, success=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = error
        self.success = success

    def mutate(self):
        pass


class CreateCourse(GenericField):
    course = graphene.Field(CourseClass)

    def __int__(self, error=None, success=True, course=None):
        super().__init__(error, success)
        self.course = course

    class Meta:
        description = "Create a new Course"

    class Arguments:
        name = graphene.String(required=True)
        duration = graphene.Float(required=True)

    def mutate(self, info, name=None, duration=None, *args, **kwargs):
        try:
            course = Course.objects.create(
                name=name,
                duration=duration,
            )

            return CreateCourse(course=course)
        except Exception as e:
            return CreateCourse(success=False, error=e)


class CreateStudent(GenericField):
    student = graphene.Field(StudentClass)

    def __int__(self, error=None, success=True, student=None):
        super().__init__(error, success)
        self.student = student

    class Meta:
        description = "Create a new student"

    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        grade = graphene.Enum.from_enum(Grades)(required=True)
        picture = Upload(required=False)
        mobiles = graphene.List(ID, required=False)
        courses = graphene.List(ID, required=False)

    def mutate(self, info, name=None, age=None, grade=None, picture=None, mobiles=None,
               courses=None, *args, **kwargs):
        try:
            print(picture, flush=True)
            student = Student(
                name=name,
                age=age,
                grade=grade,
                picture=picture
            )
            if mobiles:
                student.save()
                for mobile in mobiles:
                    Mobile.objects.create(mobile=mobile, student=student)
            if courses:
                student.save()
                student.course_set.add(*courses)
            student.save()

            return CreateStudent(student=student)
        except Exception as e:
            return CreateStudent(success=False, error=e)


class AssignCoursesToStudent(GenericField):
    student = graphene.Field(StudentClass)
    courses = graphene.List(CourseClass)

    def __int__(self, error=None, success=True, student=None, courses=None):
        super().__init__(error, success)
        self.student = student
        self.courses = courses

    class Meta:
        description = "Assign courses to student"

    class Arguments:
        student_id = graphene.ID()
        courses = graphene.List(ID)

    def mutate(self, info, student_id=None, courses=None, *args, **kwargs):
        try:
            student = Student.objects.get(id=student_id)
            student.course_set.add(*courses)
            return AssignCoursesToStudent(student=student,
                                          courses=Course.objects.filter(id__in=courses))
        except Exception as e:
            return AssignCoursesToStudent(success=False, error=e)


class AssignStudentsToCourse(GenericField):
    course = graphene.Field(CourseClass)
    students = graphene.List(StudentClass)

    def __int__(self, error=None, success=True, course=None, students=None):
        super().__init__(error, success)
        self.course = course
        self.students = students

    class Meta:
        description = "Assign students to course"

    class Arguments:
        course_id = graphene.ID()
        students = graphene.List(ID)

    def mutate(self, info, course_id=None, students=None, *args, **kwargs):
        try:
            course = Course.objects.get(id=course_id)
            course.students.add(*students)
            return AssignStudentsToCourse(course=course,
                                          students=Student.objects.filter(id__in=students))
        except Exception as e:
            return AssignStudentsToCourse(success=False, error=e)


class DeleteStudent(GenericField):
    class Meta:
        description = "Delete student"

    class Arguments:
        id = graphene.ID(required=True)

    @superuser_required
    def mutate(self, info, id, *args, **kwargs):
        try:
            Student.objects.filter(id=id).delete()

            return DeleteStudent()
        except Exception as e:
            return DeleteStudent(success=False, error=e)
