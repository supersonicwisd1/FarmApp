from django.contrib import admin

from .models import Farm, FarmerDetail, FarmingType

admin.site.register(Farm)
admin.site.register(FarmingType)
admin.site.register(FarmerDetail)