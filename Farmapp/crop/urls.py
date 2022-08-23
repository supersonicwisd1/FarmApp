from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:crop_slug>/', views.crop, name='crop'),
    path('<slug:category_slug>/', views.category, name='category'),
]
