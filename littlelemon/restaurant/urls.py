from django.urls import path
from . import views

urlpatterns = [
    path("menu", views.MenuItemsView.as_view(), name='menuitem-list'),
    path("menu/<int:pk>", views.SingleMenuItemsView.as_view(), name='menu-detail'),
    path("book", views.BookingsView.as_view(), name='book-list'),
    path("book/<int:pk>", views.SingleBookingsView.as_view(), name='book-detail')
    
    # path('', views.index, name='index'), 
    # path("booking", views.BookingView.as_view()),
    # path("menu", views.MenuView.as_view())
]