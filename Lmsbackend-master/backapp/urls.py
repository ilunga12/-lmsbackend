from django.urls import path

from backapp import views

urlpatterns = [
    path('teachers/', views.Teacher_List.as_view()),
    path('teachers/<int:pk>/', views.Teacher_Detail.as_view()),
    path('LoginView/',views.LoginView,name="LoginView"),
    path('Course_add/', views.Course_add.as_view()),
    path('CategoryList/',views.CategoryList.as_view()),
    path('Student_reg/',views.Student_reg.as_view()),
]
