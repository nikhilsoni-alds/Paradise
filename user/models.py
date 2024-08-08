from django.db import models

# Create your models here.
class CommanDetails(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)

  class Meta:
    abstract = True

class User(CommanDetails):
  OWNER='O'
  CUSTOMER='C'
  STAFF='S'
  USERTYPE_CHOICES=[(OWNER,'Owner'), (CUSTOMER, 'Customer'), (STAFF, 'Staff')]
  GENDER_CHOICES= (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),               
    )
  name=models.CharField(max_length=255)
  type=models.CharField(choices=USERTYPE_CHOICES, max_length=1, default='C')
  phone=models.CharField(max_length=15, unique=True)
  email=models.EmailField(max_length=60, unique=True, db_index=True)
  password=models.TextField()
  gender=models.CharField(choices=GENDER_CHOICES, max_length=1, default='M')


  def __str__(self) -> str:
    return self.name
