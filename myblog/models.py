from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic =  models.ImageField(null=True,blank=True, upload_to='images/profile_pic')
    facebook_url = models.CharField(max_length=500,blank=True,null=True)
    instagram_url = models.CharField(max_length=500,blank=True, null=True)
    twitter_url = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_images =models.ImageField(null=True,blank=True, upload_to='images/')
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date= models.DateField(auto_now_add= True)
    snippet = models.TextField(max_length=250,default = "Click Link Above To Read Blog Post....")
    likes=models.ManyToManyField(User,related_name='blog_posts_likes')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def  total_likes(self):
        return self.likes.count()