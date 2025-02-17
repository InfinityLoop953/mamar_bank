
from django.urls import path
from . views import UserRegistrationsView,UserLoginView,UserLogoutView
urlpatterns = [
  
    path('register/', UserRegistrationsView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView.as_view(),name='logout'),

]
