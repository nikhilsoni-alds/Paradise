from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from restaurant.models import Category, Image, Menu, MenuItems, Profile, Restaurant, Table
from restaurant.serializers import CategorySerializer, ImageSerializer, MenuItemsSerializer, MenuSerializer, RegisterStaffSerializer, RestaurantSerializer, TableSerializer
# Create your views here.

class RestaurantViewset(ModelViewSet):
  queryset = Restaurant.objects.all()
  serializer_class = RestaurantSerializer
  http_method_names = ['get', 'post', 'patch', 'delete']
  
class ImageViewset(ModelViewSet):
  queryset = Image.objects.all()
  serializer_class = ImageSerializer
  http_method_names = ['get', 'post', 'patch', 'delete']
  
class TableViewset(ModelViewSet):
  queryset = Table.objects.all()
  serializer_class = TableSerializer
  http_method_names = ['get', 'post', 'patch', 'delete']
  
class MenuViewset(ModelViewSet):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  http_method_names = ['get', 'post', 'patch', 'delete']
  
class CategoryViewset(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  http_method_names = ['get', 'post', 'patch', 'delete']
  
class MenuItemsViewset(ModelViewSet):
  queryset = MenuItems.objects.all()
  serializer_class = MenuItemsSerializer
  http_method_names = ['get', 'post', 'patch', 'delete']
  
class RegisterStaffViewset(ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = RegisterStaffSerializer
  http_method_names = ['get', 'post', 'patch', 'delete']

    