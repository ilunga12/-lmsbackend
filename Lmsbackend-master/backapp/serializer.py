from rest_framework import serializers

from backapp.models import Teacher,Student,CourseCategory,Course


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields =['id', 'full_name', 'email', 'password', 'mobile_no','qualification','skills']


class CourseaddSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id','title','description']


class StudentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'password', 'mobile_no','qualification','interested_categories']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'category', 'teacher','title','description','featured_img','technology']