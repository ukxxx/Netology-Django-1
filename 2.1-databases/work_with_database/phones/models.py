from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    image = models.ImageField(upload_to="phones/photos/")
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name + " " + self.price

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
