from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Animal(models.Model):
    SEX_CHOICES = (
        ('f', 'Female',),
        ('m', 'Male',),
        ('u', 'Unknown',),
    )
    LOCATION_CHOICES = (
        ('tl', 'Tallinn'),
        ('ta', 'Tartu'),
        ('ra', 'Rakvere'),
        ('na', 'Narva'),
        ('si', 'Sillamäe'),
        ('ku', 'Kuuresaare'),
        ('ha', 'Haapsalu'),
        ('pa', 'Pärnu'),
        ('ko', 'Kohtla-Järve'),
        ('va', 'Valga'),
        ('po', 'Põlva'),
        ('to', 'Toila'),
    )
    FUR_PATTERN_CHOICES = (
        ('t', 'Tabby'),
        ('s', 'Solid'),
        ('b', 'Bicolor'),
        ('t', 'Tortoiseshell'),
        ('c', 'Colorpoint'),
    )
    FUR_LENGTH_CHOICES = (
        ('l', 'Long'),
        ('s', 'Short'),
        ('c', 'Curly'),
        ('h', 'Hairless'),
    )

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=255)
    fur_pattern = models.CharField(max_length=1, choices=FUR_PATTERN_CHOICES, default="")
    fur_color = models.CharField(max_length=255, default='unknown')
    fur_length = models.CharField(max_length=1, choices=FUR_LENGTH_CHOICES)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    description = models.TextField(blank=True)
    special_needs = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(15.0)],)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Animals"
        ordering = ('-created',)

    def __str__(self):
        return self.animal_name