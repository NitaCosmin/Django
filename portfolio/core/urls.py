from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),         # This is your homepage
    path('contact/', views.contact, name='contact'),  # Contact page
    
]
