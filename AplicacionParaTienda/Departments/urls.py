from django.urls import path
from . import views

app_name = 'Departments'

urlpatterns = [
    path('search-department', views.SearchDepartmentListView.as_view(), name = 'searcheddepartment'),
    path('add-departments/', views.AddDepartmentsView, name = 'adddeppartmentpage'),
    path('show-departments/', views.ShowDepartmentsListView.as_view(), name = 'showdeppartmentspage'),
]
