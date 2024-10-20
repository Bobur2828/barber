from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes


# ---------------------------Reviews-------------------------------------

@api_view(['GET'])
def get_review(request):
    reviews = models.Review.objects.filter(status=True)
    reviews_sr = serializers.ReviewSerializer(reviews, many=True)

    data = {
        'reviews': reviews_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# ---------------------------Banner-------------------------------------

@api_view(['GET'])
def get_banner(request):
    banners = models.Banner.objects.all()
    banners_sr = serializers.BannerSerializer(banners, many=True)
    data = {
        'banners': banners_sr.data,
    }
    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# ---------------------------About-------------------------------------

@api_view(['GET'])
def get_about(request):
    about = models.About.objects.all()
    about_sr = serializers.AboutSerializer(about, many=True)
    data = {
        'about': about_sr.data,
    }
    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# ---------------------------Gallery-------------------------------------

@api_view(['GET'])
def get_gallery(request):
    gallery = models.Gallery.objects.all()
    gallery_sr = serializers.GallerySerializer(gallery, many=True)
    data = {
        'gallery': gallery_sr.data,
    }
    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# ---------------------------Barber-------------------------------------

@api_view(['GET'])
def get_barber(request):
    barbers = models.Barber.objects.all()
    barbers_sr = serializers.BarberSerializer(barbers, many=True)
    data = {
        'barbers': barbers_sr.data,
    }
    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })

