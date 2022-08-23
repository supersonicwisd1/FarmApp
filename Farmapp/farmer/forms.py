from django.forms import ModelForm

from crop.models import Crop
from .models import FarmerDetail

class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = ['category', 'image', 'crop_name', 'description', 'quantity', 'price', 'discount', 'delivery_type'] 
        
class ProfileForm(ModelForm):
    class Meta:
        model = FarmerDetail
        fields = ['firstname', 'lastname', 'farm_name', 'email', 'phone', 'state', 'country', 'farming_type', 'about', 'image'] 
        
