from django.urls import path
from .views import BookProfile, Inbox, BookingDetails

urlpatterns = [
    path('create/<str:pk>/', BookProfile, name='book-profile'),
    path('inbox/', Inbox, name='inbox'),
    path('details/<str:pk>/', BookingDetails, name='book-details'),
]