from django.contrib import admin
from typing import List
from import_export.admin import ImportExportModelAdmin

from restaurant.models import Category, Image, Menu, MenuItems, Profile, Restaurant, Table
# Register your models here.
class CommonActionsAndList(ImportExportModelAdmin):
    list_display: List[str] = ["created_at"]
    list_filter = [
        "created_at",
        "updated_at",
        "is_active",
    ]

@admin.register(Restaurant)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'name', 'slug', 'phone', 'email', 'owner', 'address', 'city', 'type']
    prepopulated_fields = {"slug": ["name"]}

@admin.register(Image)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'title', 'image_url', 'restaurant']

@admin.register(Table)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'table_no', 'restaurant']

@admin.register(Menu)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'name', 'restaurant']
    
@admin.register(MenuItems)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'category', 'is_veg', 'item_name', 'price', 'menu']
    
@admin.register(Category)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'name', 'menu']
    
@admin.register(Profile)
class RestaurantAdmin(CommonActionsAndList):
    list_display=['id', 'name', 'type', 'designation', 'phone', 'email', 'password', 'gender', 'restaurant']

    
