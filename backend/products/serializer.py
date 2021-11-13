from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 65,min_length = 8 ,write_only = True
    )
    email = serializers.EmailField(max_length=255,min_length = 4)
    first_name = serializers.CharField(max_length=255,min_length = 4)
    last_name = serializers.CharField(max_length=255,min_length = 4)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password']
    def validate(self, attrs):
        email = attrs.get('email',)
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        
class CategorySerializer(serializers.ModelSerializer):
    serializered_category=category_master()
    class Meta:
        model = category_master
        fields ='__all__'
class CategroyModel(serializers.ModelSerializer):
    class Meta:
        model = category_master
        fields = ['category_name',]
class SubCategorySerializer(serializers.ModelSerializer):
    category = CategroyModel()
    class Meta:
        model = subcategory_master
        fields ='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_master
        fields ='__all__'
class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction_info
        fields ='__all__'