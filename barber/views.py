from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.viewsets import ModelViewSet
from .permissions import *
from . import models
from . import serializers
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication

# ---------------------------Reviews-------------------------------------
class ReviewViewSet(ModelViewSet):
    queryset = models.Review.objects.filter(status=True)
    serializer_class = serializers.ReviewSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [CustomPermission]

# ---------------------------Banners-------------------------------------
class BannerViewSet(ModelViewSet):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

# ---------------------------Banners-------------------------------------
class AboutViewSet(ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

# ---------------------------Banners-------------------------------------
class GalleryViewSet(ModelViewSet):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]