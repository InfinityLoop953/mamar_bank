
from django.urls import path
from . views import UserRegistrationsView,UserLoginView
urlpatterns = [
  
    path('register/', UserRegistrationsView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),

]
