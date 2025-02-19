from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
from .models import UserBankAccount, UserAddress

# Create your views here.

class UserRegistrationsView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    
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
    
    
    
class UserProfileView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        user = request.user
        try:
            user_account = UserBankAccount.objects.get(user=user)
            user_address = UserAddress.objects.get(user=user)
        except UserBankAccount.DoesNotExist or UserAddress.DoesNotExist:
            user_account = None
            user_address = None

        context = {
            'user': user,
            'user_account': user_account,
            'user_address': user_address,
        }
        return render(request, self.template_name, context)
   
     
    
    
    
    

    
        
