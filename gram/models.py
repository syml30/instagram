from django.db import models

from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


#### sakht signal baray user ke profile bezare

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=350)
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    profile_avatar = models.ImageField(upload_to='AvatarPicture/')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user}"


class Image(models.Model):  # post
    image = models.ImageField(upload_to='pictsgram/')
    image_caption = models.CharField(max_length=700)
    tag_someone = models.CharField(max_length=50, blank=True)
    imageuploader_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name="images")  # <-----
    image_link = models.ManyToManyField('Profile', blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.image_caption


class Comments(models.Model):
    comment_post = models.CharField(max_length=300)
    author = models.ForeignKey('Profile', related_name='commenter', on_delete=models.CASCADE)
    commented_image = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Request(models.Model):
    pass


class Setting(models.Model):
    PROFILE_STATUS = (
        ("public", "Public"),
        ("private", "Private")
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=PROFILE_STATUS)
    image_setting = models.ImageField(upload_to='ProfilePicture/')


class Like(models.Model):
    liker = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.liker.user}"
