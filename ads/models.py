from django.db import models


class Ads(models.Model):

    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=False)


class Category(models.Model):

    name = models.CharField(max_length=30, unique=True)