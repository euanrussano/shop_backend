from rest_framework import serializers

from .models import Coupon

class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupon
        fields = ('code', 'valid_from', 'valid_to', 'discount', 'active')

