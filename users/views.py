from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import viewsets

from backend.permissions import isStaffOrReadOnly

from .serializers import UserSerializer, GroupSerializer, AddressSerializer
from .models import Address

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [isStaffOrReadOnly,]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [isStaffOrReadOnly,]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [isStaffOrReadOnly,]





