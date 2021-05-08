from django.urls import path
from . import views

app_name = 'Products'

urlpatterns = [
    path('show-all-products/', views.showproducts_view, name = 'showproductspage'),
    path('add-new-products/', views.addproducts_view, name = 'addproductspage'),
]
