# Generated by Django 4.1 on 2022-08-22 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_alter_farmerdetail_farm_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmerdetail',
            old_name='farmer_firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='farmerdetail',
            old_name='farmer_lastname',
            new_name='lastname',
        ),
    ]