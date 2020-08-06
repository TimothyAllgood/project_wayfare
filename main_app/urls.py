from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.get_posts, name='posts'),
    path('cities/', views.city_index, name='cities'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
]