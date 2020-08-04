from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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