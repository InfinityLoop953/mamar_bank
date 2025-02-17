from django.shortcuts import render
from django.views.generic import FormView,RedirectView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

class UserRegistrationsView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        return super().form_valid(form) #form valid function call hobe jodi sob thik thake
    
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
   
     
    
    
    
    

    
        
