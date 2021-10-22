from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from backend.permissions import isStaffOrReadOnly

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user', ) # filter using /?category=1

class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer