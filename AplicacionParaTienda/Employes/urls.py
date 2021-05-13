from django.urls import path
from . import views

app_name = 'Employes'

urlpatterns = [
    path('search-employe', views.SearchEmployesListView.as_view() , name = 'searchemploye'),
    path('show-all-employes/', views.ShowAllEmployesListView.as_view() , name = 'showemployespage'),
    path('add-new-employe/', views.addemploye_view, name = 'addemployespage'),
]
