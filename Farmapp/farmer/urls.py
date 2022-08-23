
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('become-farmer/', views.become_farmer, name='become_farmer'),
    path('farmer-admin/', views.farmer_admin, name='farmer_admin'),
    # path('profile/', views.profile, name='profile'),
    path('add-crop/', views.add_crop, name='add_crop'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='farmers/login.html'), name='login'),
]
