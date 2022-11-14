from django.urls import path ,re_path
from . import views

urlpatterns = [
   
    path('addEmployee/', views.EmployeeSignUpView.as_view(),name = 'emp_sign-up' ),
    path('empLogIn/', views.EmployeeSignInView.as_view(),name = 'emp_sign-in' ),


]