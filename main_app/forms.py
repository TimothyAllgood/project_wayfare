from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from .models import Profile, Post


CITIES = (
    ('S', 'San Francisco'),
    ('L', 'London'),
    )

class SignUpForm(UserCreationForm):
    city = forms.CharField(label='Current City?', widget=forms.Select(choices=CITIES))

    # city = forms.CharField(max_length=1)
    # widget = forms.Select(choices=CITIES)
    class Meta:
        model = User
        fields = ('username', 'city', 'password1', 'password2',)

# Used info from https://medium.com/@szczerbeansky/django-web-app-and-images-cloudinary-straightforward-study-ae8b5bb03e37 for Cloudinary Upload

class AvatarUploadForm(forms.ModelForm):
    city = forms.CharField(label='Current City?', widget=forms.Select(choices=CITIES))
    avatar = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'avatars'
       }
    )
    class Meta:
        model = User
        fields = ('username', 'avatar', 'city',)

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=25, required=True)
    content = forms.CharField(max_length=1000, required=True, widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = ("title", "content")
