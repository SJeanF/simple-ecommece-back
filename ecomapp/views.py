import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .products import products

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
  return Response('Hello Jenan')

@api_view(['GET'])
def getProducts(request):
  products = Product.objects.all()
  serialized = ProductSerializer(products, many=True)

  print(type(serialized.data))

  return Response(serialized.data)

@api_view(['GET'])
def getProduct(request, pk):

  product = get_object_or_404(Product, _id=pk)
  serialized = ProductSerializer(product, many=False)

  return Response(serialized.data)

