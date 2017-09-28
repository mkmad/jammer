from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class WallPosts(models.Model):

    post = models.CharField(max_length=500,
                            default=None,
                            null=True)
    image = models.ImageField(upload_to='images',
                              default=None,
                              null=True)
    videos = models.URLField(max_length=500, blank=True,
                             default=None,
                             null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/profile',
                                    default=None,
                                    null=True)
    background_pic = models.ImageField(upload_to='profile/background',
                                       default=None,
                                       null=True)
    about = models.CharField(max_length=1000,
                             default=None,
                             null=True)
    location = models.CharField(max_length=200,
                                default=None,
                                null=True)
    # posts = [objs for objs in WallPosts.objects.filter(WallPosts__user=user)]
