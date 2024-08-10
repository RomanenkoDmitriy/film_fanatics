from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True, blank=True, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=100)
    preferences = models.CharField(max_length=150)
    favorite_movie = models.CharField(max_length=200, null=True, blank=True)
    favorite_genre = models.CharField(max_length=50, null=True, blank=True)
    favorite_actor = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.first_name
