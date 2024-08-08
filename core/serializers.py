from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group, Permission


class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'username', 'password','first_name', 'last_name', 'is_active', 'is_staff']

    def create(self, validated_data):
        validated_data['password']  = make_password(validated_data['password'])
        validated_data['is_staff']=False

        return super().create(validated_data)
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        token['id'] = user.id
        return token


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['name', 'codename']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ['name','permissions']

class UserGetSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)
    email = serializers.ReadOnlyField()
    phone = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "username",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "is_mfa"
        ]