from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from user.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields='__all__'

  def create(self, validated_data):
        validated_data['password']  = make_password(validated_data['password'])
        # validated_data['is_staff']=False
        return super().create(validated_data)

