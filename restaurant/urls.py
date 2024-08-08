from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurant.views import CategoryViewset, ImageViewset, MenuItemsViewset, MenuViewset, RegisterStaffViewset, RestaurantViewset, TableViewset

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewset, basename='restaurant')
router.register(r'image', ImageViewset, basename='image')
router.register(r'table', TableViewset, basename='table')
router.register(r'menu', MenuViewset, basename='menu')
router.register(r'category', CategoryViewset, basename='category')
router.register(r'menu-items', MenuItemsViewset, basename='menu-items')
router.register(r'register-staff', RegisterStaffViewset, basename='register-staff')


urlpatterns = [
  path('', include(router.urls)),
  
]