from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status

# for sending mails and generate token
from django.utils.http import urlsafe_base64_decode
from .utils import generate_token
from django.utils.encoding import force_text
from django.views.generic import View
from .tasks import send_activation_email


from .models import Product, Order
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken, OrderSerializer

# Create your views here.
@api_view(['GET'])
def get_routes(request):
  return Response('Hello Jenan')

@api_view(['GET'])
def get_products(request):
  products = Product.objects.all()
  serialized = ProductSerializer(products, many=True)

  return Response(serialized.data)

@api_view(['GET'])
def get_product_by_id(request, pk):

  product = get_object_or_404(Product, _id=pk)
  serialized = ProductSerializer(product, many=False)

  return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request): 
  user = request.user
  serialized = UserSerializerWithToken(user, many=False)

  return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
  users = User.objects.all()
  serialized = UserSerializer(users, many=True)

  return Response(serialized.data)

class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def register_user(request):
  data = request.data
  try :
    user = User.objects.create(first_name=data['fname'], last_name=data['lname'], username=data['email'], email=data['email'], password=make_password(data['password']), is_active=False)
    
    send_activation_email(user)

    serialized = UserSerializerWithToken(user, many=False)
    return Response(serialized.data)
  except Exception as e:
    message = {'detail': f'{e}'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)

class ActivateAccountView(View):
  def get(self, request, uid64, token):
    try:
      uid = force_text(urlsafe_base64_decode(uid64))
      user = User.objects.get(id=uid)

    except Exception as e:
      user=None
    if user is not None and generate_token.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request,"activatesuccess.html")
    else:
        return render(request,"activatefail.html")   
