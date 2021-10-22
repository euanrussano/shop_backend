from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from backend.permissions import isStaffOrReadOnly

from cart.managers import CartManager

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ('category', ) # filter using /?category=1
    search_fields = ['name'] # search using /?search=<term>
    ordering_fields = ['name', 'price']

    # @action(detail=True, methods=['post'])
    # def add_to_cart(self, request, pk=None):
    #     product = self.get_object()
        
    #     quantity = int(request.data.get('quantity'))
    #     override_quantity = request.data.get('override_quantity')
    #     print('quantity = ', quantity)
    #     print('override_quantity = ', override_quantity)
    #     if quantity >= 1:
    #         cart_manager = CartManager(request)
    #         cart_manager.add(product, quantity, override_quantity=override_quantity)
    #         return Response({'status': 'product added to cart'})
    #     else:
    #         return Response({'status': 'bad quantity'})
        

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer