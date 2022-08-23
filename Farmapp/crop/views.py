import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Category, Crop

def search(request):
    query = request.GET.get('query', '')
    crops = Crop.objects.filter(Q(crop_name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'crop/search.html', {'crops': crops, 'query': query})

def crop(request, category_slug, crop_slug):
    crop = get_object_or_404(Crop, category__slug=category_slug, slug=crop_slug)
    
    similar_crops = list(crop.category.crops.exclude(id=crop.id))
    
    if len(similar_crops) >= 4:
        similar_crops = random.sample(similar_crops, 4)
        
    return render(request, 'crop/crop.html', {'crop': crop, 'similar_crops': similar_crops})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    
    return render(request, 'crop/category.html', {'category': category})