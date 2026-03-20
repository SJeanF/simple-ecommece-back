from .models import Order
from django.utils import timezone

def conclude_current_order(user):
  current_order = Order.objects.get(user=user, is_completed=False)
  current_order.is_completed = True
  current_order.closed_at = timezone.now()
  current_order.save()

  return current_order

def create_new_order(user):
  Order.objects.create(user=user)