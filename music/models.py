from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class WallPosts(models.Model):

    post = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    videos = models.URLField(max_length=500, blank=True,
                             default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/profile')
    background_pic = models.ImageField(upload_to='profile/background')
    about = models.CharField(max_length=1000)
    location = models.CharField(max_length=200)
    # posts = [objs for objs in WallPosts.objects.filter(WallPosts__user=user)]
