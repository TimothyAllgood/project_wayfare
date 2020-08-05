from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, AvatarUploadForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Temp Post Data
class Post:
    def __init__(self, title, content, author,):
        self.title = title
        self.content = content
        self.author = author
      


posts = [
   Post('Travellers guide', 'content', 'auth name'),
   Post('Top Cities', 'content', 'auth name',),
   Post('Best Dining While Travelling', 'content', 'auth name'),
]

# Create your views here.
def home(request):
    signup_form = SignUpForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form,}
    return render(request, 'home.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
            form = SignUpForm(request.POST)
            if form.is_valid():
            # This will add the user to the database
                user = form.save()
                user.refresh_from_db()
                user.profile.city = form.cleaned_data.get('city')
                user.save()
      # This is how we log a user in via code
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
    else:
        form = SignUpForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    user = request.user
    logged_user = User.objects.get(username=user)
    instance = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        print(instance)
        if form.is_valid():
            logged_user.username = request.POST['username']
            logged_user.save()
            form.save()
            return redirect('/profile')
    form = AvatarUploadForm()
    return render(request, 'registration/profile.html', {'form': form, 'posts': posts})

def posts(request, post_id,):
    return render(request, 'post.html')

