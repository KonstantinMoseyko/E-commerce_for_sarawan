from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name='имя', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='slug-имя', max_length=256, null=False, unique=True)
    image = models.ImageField(upload_to='category_img', blank=True)
    description = models.TextField(verbose_name="описание категории", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='slug-имя', max_length=256, null=False, unique=True)
    image = models.ImageField(upload_to='subcategory_img', blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('subcategory_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=256, unique=True)
    slug = models.SlugField(verbose_name='slug-имя', max_length=256, null=False, unique=True)
    image = models.ImageField(upload_to='product_img', blank=True)
    description = models.TextField(verbose_name="описание продукта", blank=True, null=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
