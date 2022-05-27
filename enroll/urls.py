from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('student/<int:pk>/uodate/', views.UpdateStudentView.as_view(), name='update_student'),
    path('student/delete/<int:pk>', views.DeleteStudentView.as_view(), name='delete_student'),
]