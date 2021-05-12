from django.urls import path
from . import views

app_name = 'Products'

urlpatterns = [
    path('search', views.SearchProductsListView.as_view(), name = 'search'),
    path('show-all-products/', views.ShowproductsListView.as_view(), name = 'showproductspage'),
    path('add-new-products/', views.addproducts_view, name = 'addproductspage'),
]
