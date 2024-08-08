from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SelfViewSet, UserViewSet
from .views import UserViewSet, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView



router = DefaultRouter()
router.register(r'register', UserViewSet,basename="register")
router.register(r'self',SelfViewSet,basename="user-self")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]