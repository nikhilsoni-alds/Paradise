from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Permission
# from core.models import User
from user.models import User
from core.serializers import MyTokenObtainPairSerializer, UserGetSerializer
from rest_framework.response import Response

from user.serializers import UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        # print(self.request.user.get_all_permissions())
        import_permission = Permission.objects.get(codename='can_import_users')
        export_permission = Permission.objects.get(codename='can_export_users')
        print("admin",import_permission, export_permission)
        return super().get_queryset()



class SelfViewSet(ModelViewSet):
    serializer_class = UserGetSerializer
    http_method_names = ['get', 'patch']
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(is_active=True)

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        queryset = queryset.filter(id=self.request.user.id).first()
        ser = self.serializer_class(queryset, many=False)
        return Response(data=ser.data)