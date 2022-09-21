from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.TextField(max_length=100)
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()