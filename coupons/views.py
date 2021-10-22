from rest_framework import viewsets

from backend.permissions import isStaffOrReadOnly

from .models import Coupon
from .serializers import CouponSerializer

# Create your views here.
class CouponViewSet(viewsets.ModelViewSet):
    permission_classes = (isStaffOrReadOnly,)
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer