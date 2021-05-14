from django.urls import path
from . import views

urlpatterns = (
    path('create-user/', views.AddUserPageView , name = "createuserpage"),
    path('', views.LoginPageView , name = "loginpage"),
    path('logout', views.Logout , name = "logoutpage"),
)