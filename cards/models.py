from django.db import models

from author.models import MyUser
from .utils import manga_photo_path

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=manga_photo_path)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='cards')
    year = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name='cards')
    synopsis = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField()
    cards = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='reviews')

