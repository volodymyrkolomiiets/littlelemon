from django.urls import path, include
from . import views



urlpatterns = [
    path("menu", views.MenuItemsView.as_view(), name='menu-detail'),
    path("menu/<int:pk>", views.SingleMenuItemsView.as_view(), name='menu-detail'),
    path("booking", views.BookingsView.as_view(), name='booking-list'),
    path("booking/<int:pk>", views.SingleBookingsView.as_view(), name='booking-detail')
    
    # path('', views.index, name='index'), 
    # path("booking", views.BookingView.as_view()),
    # path("menu", views.MenuView.as_view())
]