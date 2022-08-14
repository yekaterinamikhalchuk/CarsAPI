from django.shortcuts import render
from rest_framework import generics
from .serializers import CarDetailSerializer, CarsListSerializer
from .models import Cars
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Cars.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Cars.objects.all()
    permission_classes = (IsAdminUser, )