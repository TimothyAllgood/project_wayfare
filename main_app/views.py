from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, AvatarUploadForm, PostForm
from .models import Profile, City, Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    signup_form = SignUpForm()
    login_form = AuthenticationForm()
    if request.user.is_authenticated:
        if 'error_message' in request.session:
            del request.session['error_message']
            return redirect('profile')
    context = {'signup_form': signup_form, 'login_form': login_form}
    return render(request, 'home.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = SignUpForm(request.POST)
        print(request.POST['username'])
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
            user.refresh_from_db()
            user.profile.city = form.cleaned_data.get('city')
            user.save()
    # This is how we log a user in via code
            login(request, user)
            if 'error_message' in request.session:
                del request.session['error_message']
            return redirect('profile')
        else:
            request.session['error_message'] = 'Invalid sign up - try again'
            return redirect('home')
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
    posts = logged_user.post_set.all()
    if request.method == "POST":
        form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            logged_user.username = request.POST['username']
            if User.objects.filter(username = request.POST['username']).exists() and not logged_user.username == request.POST['username']:
                return redirect('/profile')
            else:
                logged_user.save()
                form.save()
                return redirect('/profile')
        else:
            return redirect('/profile')
    form = AvatarUploadForm()
    return render(request, 'registration/profile.html', {'form': form, 'logged_user': 'logged_user', 'posts': posts})

def get_posts(request, post_id):
    posts = Post.objects.all()
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) 
        if form.is_valid():
            post = form.save()
            return redirect('posts', post.id)
    else:
        form = PostForm(instance=post)
        author = User.objects.get(id=post.user_id)
        context = {'post': post, 'author': author, 'posts': posts, 'form': form,}
        return render(request, 'post.html', context)


def city_index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return redirect('city_detail', 1)

def city_detail(request, city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    form = PostForm(request.POST)
    user = request.user
    if request.method == 'POST':
        logged_user = User.objects.get(username=user) 
        new_post = form.save(commit=False)
        new_post.city_id =  city_id
        new_post.user_id =  logged_user.id
        new_post.save()
        return redirect('city_detail', city_id)
    else:
        context = {'cities': cities, 'city': city, "form": form, }
        return render(request, 'cities/city.html', context)

def delete_post(request, post_id):
    Post.objects.get(id = post_id).delete()
    first_post = Post.objects.all().first()
    if Post.objects.all().count() > 0:
        return redirect('posts', first_post.id)    
    else:
        return redirect('home')
        
