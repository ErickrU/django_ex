"""db_img_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import *
from image_storage.views import client_img_view, products_img_view, order_img_view
from django.conf import settings
from django.conf.urls.static import static
from image_storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #client
    path('client_form/', client_img_view.as_view(), name="form_client"),
    path('list_client/', views.print_client, name="client_display"),
    path('update_client/<int:id>', client_img_view.as_view(), name="update_client"), 
    path('delete_client/<int:id>', views.delete_client, name="delete_client"),
    #products
    path('products_form/', products_img_view.as_view(), name="form_products"),
    path('list_products/', views.print_products, name="products_display"),
    path('update_products/<int:id>', products_img_view.as_view(), name="update_products"), 
    path('delete_products/<int:id>', views.delete_products, name="delete_products"),
    #order
    path('order_form/', order_img_view.as_view(), name="form_order"),
    path('list_order/', views.print_order, name="order_display"),
    path('update_order/<int:id>', order_img_view.as_view(), name="update_order"), 
    path('delete_order/<int:id>', views.delete_order, name="delete_order"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)