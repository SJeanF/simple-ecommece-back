from ecomapp import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
  path('', views.get_routes, name='get_routes'),
  path('products/', views.get_products, name='get_products'),
  path('product/<int:pk>', views.get_product_by_id, name='get_product'),
  path('user/', views.get_user_profile, name='get_user_profile'),
  path('users/', views.get_users, name='get_users'),
  path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
  path('signup/', views.register_user, name='register_user'),
  path('activate/<uid64>/<token>', views.ActivateAccountView.as_view(), name='activate_account'),
  path('orders/', views.get_all_orders_from_user, name='get_orders'),
  path('order/current/', views.get_current_order, name='get_current_order'),
  path('order/close/', views.checkout_order, name='checkout_order'),
  path('order-item/create/', views.create_update_order, name='create_order_item'),
  path('order-item/delete', views.delete_order_item, name='delete_order_item')
]