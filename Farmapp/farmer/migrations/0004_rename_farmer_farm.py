# Generated by Django 4.1 on 2022-08-22 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmer', '0003_remove_farmer_country_remove_farmer_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Farmer',
            new_name='Farm',
        ),
    ]
