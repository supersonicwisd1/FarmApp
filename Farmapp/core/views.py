from django.shortcuts import render

from crop.models import Crop

def home(request):
    newest_crops = Crop.objects.all()[0:8]
    return render(request, 'core/home.html', {'newest_crops': newest_crops})