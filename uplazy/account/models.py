from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    expertise = models.CharField(default='no job',max_length=100, null=True, blank=True)
    profile_image = models.ImageField(default='profile-photo.png', null=True, blank=True, )
    about_me = models.TextField(default='no data',max_length=1000, null=True, blank=True)
    hourly_rate = models.IntegerField(default=5,null=True, blank=True) # in dollars
    is_artisan = models.BooleanField(default=False, null=True, blank=True) 
    country = models.CharField(default='Morocco', max_length=30, null=True, blank=True)
    city = models.CharField(default='Rabat', max_length=30, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self) -> str:
        return self.user.username
    

class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    artisan = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    content = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self) -> str:
        return self.content


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, 
            name=user.username,
        )   

def deleteUser(sender, instance,  **kwargs):
    user = instance.user    
    user.delete()

post_delete.connect(deleteUser, sender=Profile)
post_save.connect(createProfile, sender=User)