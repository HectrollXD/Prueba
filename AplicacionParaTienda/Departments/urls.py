from django.urls import path
from . import views

app_name = 'Departments'

urlpatterns = [
    path('departments/', views.departments_view, name = 'showdeppartmentspage'),
]
