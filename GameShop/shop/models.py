from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=70, unique=True, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos")
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    publisher = models.CharField(max_length=70)
    age_limited = models.BooleanField(default=True)
    genre = models.ManyToManyField("Genre", related_name="genre")

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
