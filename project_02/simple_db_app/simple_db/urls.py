from django.urls import path, include
from . import views


urlpatterns = [
    # Client
    path('insert_client', views.insert_client, name="insert_client"),
    path('list_client/', views.select_client, name="select_clients"),
    path('update_client/<int:id>', views.insert_client, name="update_client"), 
    path('delete_client/<int:id>', views.delete_client, name="delete_client"),
    # products
    path('insert_products', views.insert_products, name="insert_products"),
    path('list_product/', views.select_products, name="select_products"),
    path('update_products/<int:id>', views.insert_products, name="update_products"), 
    path('delete_products/<int:id>', views.delete_products, name="delete_products"),
    # orders
    path('insert_order', views.insert_order, name="insert_order"),
    path('list_order/', views.select_order, name="select_order"),
    path('update_order/<int:id>', views.insert_order, name="update_order"), 
    path('delete_order/<int:id>', views.delete_order, name="delete_order"),
]

