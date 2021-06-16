from django.shortcuts import render
from .models import Producto, Marca, Boleta, Despacho
from rest_framework import viewsets
from .serializers import ProductoSerializer, MarcaSerializer, BoletaSerializer, DespachoSerializer
# Create your views here.

class BoletaViewset(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DespachoViewset(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    



class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer