# Generated by Django 3.2.9 on 2021-11-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20211121_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]