from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField



class City(models.Model):
    name = models.CharField(
        max_length=250,
    )
    class Meta:
        verbose_name_plural = 'Cities'

cities = City.objects.all()

CITIES = []

for i, city in enumerate(cities):
    CITIES.append((city.name[0],city.name,),)

class Profile(models.Model):
    avatar = CloudinaryField('avatar')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(
        'City Choice',
        max_length=1,
        choices=CITIES,
        default=CITIES[0][0]
        )
    dark_mode = models.BooleanField()
    bio = models.CharField(max_length=1000)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
