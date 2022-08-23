from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from farmer.models import Farm

class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['ordering']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class Crop(models.Model):
    category = models.ForeignKey(Category, related_name='crops', on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farm, related_name='crops', on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField()
    delivery_type = models.CharField(max_length=300, null=True, choices=(
        ('farm-to-door', 'Farm to door'),
        ('pickup', 'Pick Up')
    ))
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.crop_name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return self.thumbnail.url
            else:
                return "http//via.placeholder.com/240x180.jpg"
            
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail  = File(thumb_io, name=image.name)
        
        return thumbnail
    