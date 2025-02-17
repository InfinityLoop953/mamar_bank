
from django.urls import path
from . views import UserRegistrationsView
urlpatterns = [
  
    path('register/', UserRegistrationsView.as_view(),name='register'),
]
