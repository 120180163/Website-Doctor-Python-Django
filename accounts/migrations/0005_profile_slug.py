# Generated by Django 3.0.3 on 2020-04-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200405_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]
