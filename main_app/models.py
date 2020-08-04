from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

CITIES = (
    ('S', 'San Francisco'),
    ('L', 'London'),
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(
        'City Choice',
        max_length=1,
        choices=CITIES,
        default=CITIES[0][0]
        )

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
