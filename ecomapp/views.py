from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
# from .products import products

from .models import Product
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
  return Response('Hello Jenan')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
  products = Product.objects.all()
  serialized = ProductSerializer(products, many=True)

  return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProduct(request, pk):

  product = get_object_or_404(Product, _id=pk)
  serialized = ProductSerializer(product, many=False)

  return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request): 
  user = request.user
  serialized = UserSerializerWithToken(user, many=False)

  return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
  users = User.objects.all()
  serialized = UserSerializer(users, many=True)

  return Response(serialized.data)

class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
  data = request.data
  try :
    user = User.objects.create(first_name=data['fname'], last_name=data['lname'], username=data['email'], email=data['email'], password=make_password(data['password']))
    serialized = UserSerializerWithToken(user, many=False)
    print(serialized)
    return Response(serialized.data)
  except Exception as e:
    message = {'deatil': f'{e}'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)