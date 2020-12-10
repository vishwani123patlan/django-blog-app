#from . import views
from .views import UserRegisterView , UserChangeView ,EditPasswordView, ProfileView , ProfileCreateView
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
   # path('',views.home , name='home')
  path('register/',UserRegisterView.as_view(),name='register'),
  path('edit_profile/',UserChangeView.as_view(), name='edit-profile'),
  path('password/',EditPasswordView.as_view(),name='password-change'),
  path('add_profile_details/',ProfileCreateView.as_view(),name="add_profile_detail"),
  path('<int:pk>/profile',ProfileView.as_view(),name="profile_post"),
    
]
