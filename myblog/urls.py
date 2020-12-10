#from . import views
from .views import HomeView , ArticalDetailView, AddPostView,UpdatePostView,DeletePostView,LikeView
from django.urls import path

urlpatterns = [
   # path('',views.home , name='home')
   path('',HomeView.as_view(),name="home"),
   path('artical/<int:pk>',ArticalDetailView.as_view(),name="detail-view"),
   path('addpost/',AddPostView.as_view(),name="add-post"),
   path('article/edit/<int:pk>', UpdatePostView.as_view(),name='update-view'),
   path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete-post'),
   path('like/<int:pk>',LikeView,name="like_post"),
  # path('profile/',ProfileView.as_view(),name="profile_post"),
    
]
