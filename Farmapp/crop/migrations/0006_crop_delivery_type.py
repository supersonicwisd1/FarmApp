# Generated by Django 4.1 on 2022-08-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0005_remove_crop_delivery_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='delivery_type',
            field=models.CharField(choices=[('farm-to-door', 'Farm to door'), ('pickup', 'Pick Up')], max_length=300, null=True),
        ),
    ]
