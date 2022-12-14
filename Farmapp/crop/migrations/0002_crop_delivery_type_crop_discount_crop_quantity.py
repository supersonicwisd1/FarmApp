# Generated by Django 4.1 on 2022-08-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='delivery_type',
            field=models.CharField(choices=[('farm-to-door', 'Farm to door'), ('pickup', 'Pick Up')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
