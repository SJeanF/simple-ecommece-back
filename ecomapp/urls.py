from ecomapp import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
  path('', views.get_routes, name='getRoutes'),
  path('products/', views.get_products, name='getProducts'),
  path('product/<int:pk>', views.get_product_by_id, name='getProduct'),
  path('user/', views.get_user_profile, name='getUserProfile'),
  path('users/', views.get_users, name='getUsers'),
  path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
  path('signup/', views.register_user, name='registerUser'),
  path('activate/<uid64>/<token>', views.ActivateAccountView.as_view(), name='activateAccount'),
  path('Dtest/', views.remove_test_user, name='remove_test')
]