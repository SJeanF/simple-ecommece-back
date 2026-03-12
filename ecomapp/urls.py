from ecomapp import views
from django.urls import path

urlpatterns = [
  path('', views.getRoutes, name='getRoutes'),
  path('products/', views.getProducts, name='getProducts'),
  path('product/<int:pk>', views.getProduct, name='getProduct'),
  path('user/', views.getUserProfile, name='getUserProfile'),
  path('users/', views.getUsers, name='getUsers')
]