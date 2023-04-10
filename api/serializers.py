from .models import User
from rest_framework import serializers
from .models import Product, Order, Cart


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
