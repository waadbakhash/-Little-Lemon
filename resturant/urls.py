from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),

    # Menu endpoints
    path('menu-items/', views.MenuItemList.as_view(), name='menu'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', views.msg),

    # Booking endpoint
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
