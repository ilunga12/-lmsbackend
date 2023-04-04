from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions

from backapp.models import Teacher,CourseCategory,Student,Course
from backapp.serializer import TeacherSerializer,CourseaddSerilizer,StudentSerilaizer,CourseSerializer


# Create your views here.
class Teacher_List(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Teacher_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

def LoginView(request):
    email = request.POST['email']
    password = request.POST['password']
    teacherData = Teacher.objects.get(email=email, password=password)
    if teacherData:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})



class Course_add(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseaddSerilizer

class Student_reg(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilaizer