from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from resturant import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'tables', views.BookingViewSet, basename='booking-api')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('restaurant/', include('resturant.urls')),

    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
