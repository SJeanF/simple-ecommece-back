from ecomapp import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
  path('', views.getRoutes, name='getRoutes'),
  path('products/', views.getProducts, name='getProducts'),
  path('product/<int:pk>', views.getProduct, name='getProduct'),
  path('user/', views.getUserProfile, name='getUserProfile'),
  path('users/', views.getUsers, name='getUsers'),
  path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
  path('signup/', views.registerUser, name='registerUser'),
  path('activate/<uid64>/<token>', views.ActivateAccountView.as_view(), name='activateAccount'),
  path('Dtest/', views.remove_testUser, name='remove_test')
]