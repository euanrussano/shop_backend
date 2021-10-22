from rest_framework import viewsets

from backend.permissions import isStaffOrReadOnly

from .models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer