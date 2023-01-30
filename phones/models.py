from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)
