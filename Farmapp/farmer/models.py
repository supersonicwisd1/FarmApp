from io import BytesIO
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from PIL import Image


class Farm(models.Model):
    farm_name = models.CharField(max_length= 300)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='farmer', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['farm_name']
        
    def __str__(self):
        return self.farm_name
    
    
class FarmingType(models.Model):
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class FarmerDetail(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    farm_name = models.ForeignKey(Farm, related_name='farm', on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.IntegerField()
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    farming_type = models.ForeignKey(FarmingType, related_name='farming_type', on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    
    image = models.ImageField(upload_to='media/uploads/farmers', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media/uploads/farmers', blank=True, null=True)
        
    def __str__(self):
        return self.farm_name
    
    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        
        super().save(*args, **kwargs)
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)
        
        thumbnail  = File(thumb_io, name=image.name)
        
        return thumbnail
