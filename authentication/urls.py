from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('token/', TokenObtainPairView.as_view(), name='token'),  
  path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),  
  path('token/verify/', TokenRefreshView.as_view(), name='token-refresh'),  
]