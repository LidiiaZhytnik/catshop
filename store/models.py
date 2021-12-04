from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class AnimalManager(models.Manager):
    def get_queryset(self):
        return super(AnimalManager,self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Animal(models.Model):
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Unknown', 'Unknown',),
    )
    LOCATION_CHOICES = (
        ('Tallinn', 'Tallinn'),
        ('Tartu', 'Tartu'),
        ('Rakvere', 'Rakvere'),
        ('Narva', 'Narva'),
        ('Sillamae', 'Sillamäe'),
        ('Kuuresaare', 'Kuuresaare'),
        ('Haapsalu', 'Haapsalu'),
        ('Parnu', 'Pärnu'),
        ('Kohtla-jarve', 'Kohtla-Järve'),
        ('Valga', 'Valga'),
        ('Polva', 'Põlva'),
        ('Toila', 'Toila'),
        ('EU', 'EU'),
        ('Estonia', 'Estonia'),
        ('Non-EU', 'Non-EU'),
    )
    FUR_PATTERN_CHOICES = (
        ('Tabby', 'Tabby'),
        ('Solid', 'Solid'),
        ('Bicolor', 'Bicolor'),
        ('Tortoiseshell', 'Tortoiseshell'),
        ('Colorpoint', 'Colorpoint'),
    )
    FUR_LENGTH_CHOICES = (
        ('Long', 'Long'),
        ('Short', 'Short'),
        ('Curly', 'Curly'),
        ('Hairless', 'Hairless'),
    )

    category = models.ForeignKey(Category, related_name='animal', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='animal_creator', on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=255)
    fur_pattern = models.CharField(max_length=15, choices=FUR_PATTERN_CHOICES, default="")
    fur_color = models.CharField(max_length=255, default='unknown')
    fur_length = models.CharField(max_length=15, choices=FUR_LENGTH_CHOICES)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.CharField(max_length=15, choices=SEX_CHOICES)
    location = models.CharField(max_length=15, choices=LOCATION_CHOICES)
    description = models.TextField(blank=True)
    special_needs = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(15.0)])
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    animals = AnimalManager()

    class Meta:
        verbose_name_plural = "Animals"
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:animal_detail', args=[self.slug])

    def __str__(self):
        return self.animal_name