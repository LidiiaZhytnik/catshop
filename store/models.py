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
        ('f', 'female',),
        ('m', 'male',),
        ('u', 'unknown',),
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
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=255)
    fur_color = models.CharField(max_length=255, default='unknown')
    fur_length = models.CharField(max_length=255, default='unknown')
    age = models.DecimalField(max_digits=2, decimal_places=2)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
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