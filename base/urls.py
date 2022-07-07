from django.urls import path
from .views import get_books



urlpatterns = [
    path('get/', get_books, name='get_books'),
    path('get/<int:pk>/', get_books, name='get_books'),
]