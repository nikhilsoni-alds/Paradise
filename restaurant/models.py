from django.db import models

from user.models import User

# Create your models here.
class CommanDetails(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)

  class Meta:
    abstract = True

class Restaurant(CommanDetails):
  VEGETERIAN='V'
  NON_VEGETERIAN='NV'
  BOTH='B'
  REST_TYPE_CHOICES=[(VEGETERIAN, 'Vegeterian'), (NON_VEGETERIAN, 'Non Vegeterian'), (BOTH, 'Both')]
  name=models.CharField(max_length=255)
  slug=models.SlugField()
  phone=models.CharField(max_length=15)
  email=models.EmailField(max_length=60, unique=True, db_index=True)
  owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_name', db_index=True)
  address=models.TextField()
  city=models.CharField(max_length=50)
  type=models.CharField(choices=REST_TYPE_CHOICES, max_length=2, default='V' )
  # image=models
  # timing=
  
  def __str__(self) -> str:
    return self.name


class Image(CommanDetails):
  title=models.CharField(max_length=100)
  image_url=models.ImageField(upload_to='restaurant')
  restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_image', db_index=True)

  def __str__(self) -> str:
    return self.title

class Table(CommanDetails):
  table_no=models.CharField(max_length=20)
  restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_name', db_index=True)

  def __str__(self) -> str:
    return self.table_no
  
class Menu(CommanDetails):
  name=models.CharField(max_length=50)
  restaurant=models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='restaurant_menu', db_index=True)

  def __str__(self) -> str:
    return self.name

class Category(CommanDetails):
  name=models.CharField(max_length=50)
  menu=models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_category', db_index=True)

  def __str__(self) -> str:
    return self.name

class MenuItems(CommanDetails):
  category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', db_index=True)
  is_veg=models.BooleanField(default=True)
  item_name=models.CharField(max_length=100)
  price=models.IntegerField()
  menu=models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_menuitems', db_index=True)

  def __str__(self) -> str:
    return self.item_name

class Profile(CommanDetails):
  OWNER='O'
  STAFF='S'
  USERTYPE_CHOICES=((OWNER,'Owner'), (STAFF, 'Staff'))
  GENDER_CHOICES= (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),               
    )
  SWEEPER='S'
  CHEF='CH'
  WAITER='W'
  CASHIER='CA'
  RESTAURANT_MANAGER='RM'
  DISHWASHER='DW'
  SECURITY_GUARD='SG'
  DESIGNATION_CHOICES=((SWEEPER,'Sweeper'), (CHEF, 'Chef'), (WAITER, 'Waiter'), (CASHIER, 'Cashier'), (RESTAURANT_MANAGER, 'Restaurant Manager'), (DISHWASHER, 'Dishwasher'), (SECURITY_GUARD, 'Security Guard'))
  name=models.CharField(max_length=255)
  type=models.CharField(choices=USERTYPE_CHOICES, max_length=1, default='C')
  designation=models.CharField(choices=DESIGNATION_CHOICES, max_length=3, blank=True, null=True)
  phone=models.CharField(max_length=15, unique=True)
  email=models.EmailField(max_length=60, unique=True, db_index=True)
  password=models.TextField()
  gender=models.CharField(choices=GENDER_CHOICES, max_length=1, default='M')
  restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_profile', db_index=True)

  def __str__(self) -> str:
    return self.name
  