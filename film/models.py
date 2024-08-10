from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
