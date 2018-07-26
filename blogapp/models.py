from __future__ import unicode_literals
from django.db import models
from django.conf import settings
#from django.contrib.auth import get_user_model
from django.db.models import ForeignKey
from django.urls import reverse
from django.db.models.signals import post_save


class Post (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0, null=True,)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, null=True)
    draft = models.BooleanField(default=False)
    image = models.ImageField(
                              null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogapp:details", args=(self.id,))


class Postman (models.Model):
    user = models.ForeignKey.swappable=False
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, null=True)
    draft = models.BooleanField(default=False)
    image = models.ImageField(
                              null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogapp:details", args=(self.id,))



