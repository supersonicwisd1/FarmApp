# Generated by Django 4.1 on 2022-08-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_alter_crop_delivery_type_alter_crop_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='delivery_type',
            field=models.CharField(choices=[('farm-to-door', 'Farm to door'), ('pickup', 'Pick Up')], max_length=300, null=True),
        ),
    ]
