from rest_framework import serializers

from .models import Product, Category, ProductImage

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
     )
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'category', 'description', 'images')



