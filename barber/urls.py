from django.urls import path
from . import views

app_name = 'barber'

urlpatterns = [
    path('reviews/', views.get_review),
    path('about/', views.get_about),
    path('banner/', views.get_banner),
    path('gallery/', views.get_gallery),
    path('barber/', views.get_barber),
]