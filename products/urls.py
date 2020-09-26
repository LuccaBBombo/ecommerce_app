from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_info, name='product_info'), # Added the 'int:' so that the product id is rendered as a integer
    path('add/', views.add_products, name='add_products'),
]
