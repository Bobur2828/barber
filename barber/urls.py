from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'barber'

router = routers.DefaultRouter()
router.register('reviews', views.ReviewViewSet),
router.register('banners', views.BannerViewSet),
router.register('about', views.AboutViewSet),
router.register('gallery', views.GalleryViewSet),


urlpatterns = [
    path('', include(router.urls)),
]