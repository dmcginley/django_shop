from django.db import models
from django.core.files import File
import os


class Book(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    # name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    authors = models.CharField(max_length=254)

    # image_file = models.ImageField(upload_to='images', null=True, blank=True)
    main_picture_medium = models.URLField(
        max_length=1024, null=True, blank=True)

    main_picture_large = models.URLField(
        max_length=1024, null=True, blank=True)
    alternative_titles_en = models.CharField(
        max_length=254,  null=True, blank=True)
    alternative_titles_ja = models.CharField(
        max_length=254,  null=True, blank=True)
    synopsis = models.TextField()
    mean = models.CharField(max_length=254)
    genres = models.CharField(max_length=254)

    def __str__(self):
        return self.name
