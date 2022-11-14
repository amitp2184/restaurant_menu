from django.urls import path ,re_path
from . import views

urlpatterns = [
   
    path('signUp/', views.UserSignUpView.as_view(),name = 'sign-up' ),
    path('signIn/', views.UserSignInView.as_view(),name = 'sign-in' ),

]