from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

from .models import Address

# Create your views here.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  get_user_model()
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ['url', 'name']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Address
        fields = ['url', 'user', 'address', 'postal_code', 'neighborhood', 'city', 'state', 'created', 'updated']