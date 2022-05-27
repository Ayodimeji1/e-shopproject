from django.db import models

from datetime import datetime
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# from pilkit.processors import Thumbnail

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',blank=False, default=False)

    class Meta:
        ordering = ['ordering']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('In Stock', 'In Stock'),
        ('Sale', 'Sale'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default='In Stock')

    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    added_on = models.DateTimeField(default=datetime.now, blank=True)

    image = models.ImageField(upload_to='images/', blank=False)
    thumbnail = ImageSpecField(source='images',
                               processors=[ResizeToFill(90, 80)],
                               format='JPEG',
                               options={'quality': 90})

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=False)
    thumbnail = ImageSpecField(source='images',
                               processors=[ResizeToFill(90, 80)],
                               format='JPEG',
                               options={'quality': 90})