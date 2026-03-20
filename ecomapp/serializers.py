from rest_framework import serializers
from .models import Product, Order, OrderItem
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
  _id = serializers.SerializerMethodField(read_only=True)
  name = serializers.SerializerMethodField(read_only=True)
  isAdmin = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = User
    fields = ['_id', 'id', 'username', 'name', 'email', 'isAdmin']

  def get__id(self, userObj):
    return userObj.id
  
  def get_name(self, userObj):
    firstName = userObj.first_name
    lastName = userObj.last_name

    name = f'{firstName} {lastName}' 

    if name != ' ':
      return name
    else:
      return userObj.email[:5]
  
  def get_isAdmin(self, userObj):
    return userObj.is_staff
    
class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','_id','username','email','name','isAdmin','token']
    
    def get_token(self,userObj):
        token=RefreshToken.for_user(userObj)
        return str(token.access_token)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
    serialized = UserSerializerWithToken(self.user).data
    for k, v in serialized.items():
      data[k] = v
    return data
  
class OrderItemSerializer(serializers.ModelSerializer):
  product = ProductSerializer(many=False)

  class Meta:
    model = OrderItem
    fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True, read_only=True)

  class Meta:
    model = Order
    fields = '__all__'