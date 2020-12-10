from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms  import SignUpForm , EditProfileForm , EditPasswordForm, ProfileForm , ProfileCreateForm
from myblog.models import  Profile
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserChangeView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class EditPasswordView(PasswordChangeView):
    form_class = EditPasswordForm
    template_name = 'registration/edit_password.html'
    #message = messages.success(request,'Your password is changed successfully')
    success_url = reverse_lazy('edit-profile')


class ProfileCreateView(generic.CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'registration/profile_create.html'
    


class ProfileView(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')

   