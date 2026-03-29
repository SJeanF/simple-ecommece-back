from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Order, Product, OrderItem

def conclude_current_order(user):
  order = get_object_or_404(Order,user=user, is_completed=False)
  order.is_completed = True
  order.closed_at = timezone.now()
  for item in order.items.all():
    item.date_price = item.product.price
    item.save()
  order.save()

  return order

def create_new_order(user):
  Order.objects.create(user=user)

def add_or_update_order_item(user, item_id, item_quantity):
  order = get_object_or_404(Order, user=user, is_completed=False)
  product = get_object_or_404(Product, _id=item_id)

  aready_in_order = order.items.filter(product___id=item_id).exists()
  if aready_in_order:
    order_item = OrderItem.objects.get(product___id=item_id, order=order)
    order_item.quantity = item_quantity
    order_item.save()
  else: 
    OrderItem.objects.create(product=product, quantity=item_quantity, order=order)

  return order

def detele_item(user, id):
  order = get_object_or_404(Order, user=user, is_completed=False)
  exist = order.items.filter(product___id=id).exists()

  if exist:
    order.items.get(product___id=id).delete()
    return order
  else:
    raise Exception('The requested item could not be found.')