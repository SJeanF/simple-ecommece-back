from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone

def conclude_current_order(user):
  current_order = Order.objects.get(user=user, is_completed=False)
  current_order.is_completed = True
  current_order.closed_at = timezone.now()
  current_order.save()

  serialized_current_order = OrderSerializer(current_order, many=False)
  return serialized_current_order.data

def create_new_order(user):
  Order.objects.create(user=user)
