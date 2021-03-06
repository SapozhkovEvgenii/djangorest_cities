from django.contrib import admin
from django.urls import path, include, re_path
from city.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)


# router = routers.DefaultRouter()
# router.register(r'cities', CityViewSet, basename="city")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls))
    path('api/v1/citylist/', CityAPIList.as_view()),
    path('api/v1/citylist/<int:pk>/', CityAPIUpdate.as_view()),
    path('api/v1/citydetail/<int:pk>/', CityAPIDetail.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
