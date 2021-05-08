from django.urls import path
from . import views

app_name = 'Employes'

urlpatterns = [
    path('show-all-employes/', views.showemployes_view , name = 'showemployespage'),
    path('add-new-employe/', views.addemploye_view, name = 'addemployespage'),
]
