from django import forms
from .models import Post ,Profile

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post

        fields = ('title','post_images','author','body','snippet')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'elder'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-cotrol'}),
            'snippet': forms.Textarea(attrs={'class':'form-cotrol'}),
            'post_images': forms.ClearableFileInput(attrs={'class':'form-cotrol'}),

        }


class EditPostForm(forms.ModelForm):
    
    class Meta:
        model = Post

        fields = ('title','body')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-cotrol'}),

        }


# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile

#         fields = ('bio','profile_pic','facebook_url','instagram_url','twitter_url')

#         widgets = {
#             'bio': forms.Textarea(attrs={'class':'form-control'}),
#             'profile_pic': forms.ClearableFileInput(attrs={'class':'form-control'}),
#             'facebook_url': forms.TextInput(attrs={'class':'form-cotrol'}),
#             'instagram_url': forms.TextInput(attrs={'class':'form-cotrol'}),
#             'twitter_url': forms.TextInput(attrs={'class':'form-cotrol'}),
#         }


        