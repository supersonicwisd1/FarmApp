# Generated by Django 4.1 on 2022-08-22 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_farmingtype_farmer_country_farmer_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='farmer_firstname',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='farmer_lastname',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='farming_type',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='thumbnail',
        ),
        migrations.CreateModel(
            name='FarmerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_firstname', models.CharField(max_length=300)),
                ('farmer_lastname', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/uploads/farmers')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='media/uploads/farmers')),
                ('farming_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farming_type', to='farmer.farmingtype')),
            ],
        ),
    ]
