from django.shortcuts import render
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
def getProducts(resquest):
  products = Product.objects.all()
  serialized = ProductSerializer(products, many=True)

  return Response(serialized.data)