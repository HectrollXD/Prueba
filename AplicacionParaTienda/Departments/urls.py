from django.urls import path
from . import views

app_name = 'Departments'

urlpatterns = [
    path('show-all-departments/', views.showdepartments_view, name = 'showdeppartmentspage'),
    path('add-new-department/', views.adddepartment_view, name = 'adddeppartmentpage'),
]
