from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from restaurant.models import Category, Image, Menu, MenuItems, Profile, Restaurant, Table


class RestaurantSerializer(serializers.ModelSerializer):
  images=serializers.SerializerMethodField(method_name='get_images')
  
  def get_images(self, obj):
    image=Image.objects.filter(restaurant=obj.id)
    serializer=ImageSerializer(image, many=True)
    return serializer.data

  class Meta:
    model=Restaurant
    fields='__all__'
  
class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model=Image
    fields=['id', 'title', 'image_url', 'restaurant']
  
class TableSerializer(serializers.ModelSerializer):
  class Meta:
    model=Table
    fields=['id', 'table_no', 'restaurant']
  
class MenuSerializer(serializers.ModelSerializer):
  # restaurant = serializers.CharField()
  category=serializers.SerializerMethodField(method_name='get_category')
  class Meta:
    model=Menu
    fields=['id', 'name', 'category', 'restaurant']
  def get_category(self, obj):
    data = Category.objects.filter(menu=obj.id)
    serializer = CategorySerializer(data, many=True)
    return serializer.data
  
class CategorySerializer(serializers.ModelSerializer):
  menu_items=serializers.SerializerMethodField(method_name='get_menu_items')
  class Meta:
    model=Category
    fields=['id', 'name', 'menu_items']
  
  def get_menu_items(self, obj):
    data = MenuItems.objects.filter(menu=obj.id)
    serializer = MenuItemsSerializer(data, many=True)
    return serializer.data
  
class MenuItemsSerializer(serializers.ModelSerializer):
  class Meta:
    model=MenuItems
    fields=['id', 'category', 'is_veg', 'item_name', 'price', 'menu']

class RegisterStaffSerializer(serializers.ModelSerializer):
  class Meta:
    model=Profile
    fields=['id', 'name', 'type', 'phone', 'email', 'password', 'gender', 'restaurant']
    
  def create(self, validated_data):
    validated_data['password']  = make_password(validated_data['password'])
    return super().create(validated_data)



