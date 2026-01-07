from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Menu endpoints
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),

    # Booking endpoint
    path('booking/', views.BookingView.as_view(), name='booking'),

]
