# Generated by Django 3.2.9 on 2021-11-21 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_animal_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='price',
            field=models.FloatField(default='0', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(15.0)]),
        ),
    ]
