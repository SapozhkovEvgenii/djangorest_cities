from django.contrib import admin
from django.urls import path, include
from city.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cities', CityViewSet, basename="city")
print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
    # path('api/v1/citylist/', CityViewSet.as_view()),
    # path('api/v1/citylist/<int:pk>/', CityViewSet.as_view()),
]
