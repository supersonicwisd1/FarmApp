from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify 
from django.shortcuts import render, redirect

from .models import Farm
from crop.models import Crop

from .forms import CropForm, ProfileForm

def become_farmer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            farmer = Farm.objects.create(farm_name=user.username, created_by=user)
            
            return redirect('home')
    else:
        form = UserCreationForm()
                                           
    return render(request, 'farmers/become_farmer.html', {'form': form})

@login_required
def farmer_admin(request):
    farmer = request.user.farmer
    crops = farmer.crops.all()
    
    return render(request, 'farmers/farmer_admin.html', {'farmer': farmer, 'crops':crops})

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             profile = form.save(commit=False)

#             profile.save()
            
#             return redirect('farmer_admin')
        
#     else:
#         form = ProfileForm()
#     return render(request, 'farmers/profile.html', {'form': form})

@login_required
def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)
        
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farmer = request.user.farmer
            crop.slug = slugify(crop.crop_name)
            crop.save()
            
            return redirect('farmer_admin')
        
    else:
        form = CropForm()
    return render(request, 'farmers/add_crop.html', {'form': form})