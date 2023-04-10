from django.contrib.auth import authenticate
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
def registration(request):
    serializer = serializers.RegistrationSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    token, created = Token.objects.get_or_create(user=user)

    return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_200_OK)


@api_view(["POST"])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    authenticate(email=email, password=password)
    user = User.objects.get(email=email)
    token, created = Token.objects.get_or_create(user=user)

    return Response({"token": token.key}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response({"message": "No Data"}, status=204)


class ProductListView(APIView):
    @permission_classes([AllowAny])
    def get(self, request):
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)

    @permission_classes([IsAdminUser])
    def post(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"product": serializer.data}, status=status.HTTP_201_CREATED)


class ProductDetailView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request, pk):
        try:
            product = models.Product.objects.get(id=pk)
        except models.Product.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ProductSerializer(product)
        return Response({"product": serializer.data}, status=status.HTTP_200_OK)

    @permission_classes([IsAdminUser])
    def patch(self, request, pk):
        try:
            product = models.Product.objects.get(id=pk)
        except models.Product.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ProductSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": serializer.data}, status=status.HTTP_200_OK)

    @permission_classes([IsAdminUser])
    def delete(self, request, pk):
        try:
            product = models.Product.objects.get(id=pk)
        except models.Product.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "no data"}, status=status.HTTP_204_NO_CONTENT)


class OrderListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        orders = models.Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"order": serializer.data}, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    def get(self, request, pk):
        try:
            order = models.Order.objects.get(id=pk)
        except models.Order.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ProductSerializer(order)
        return Response({"order": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            order = models.Order.objects.get(id=pk)
        except models.Order.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.ProductSerializer(data=request.data, instance=order)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            order = models.Order.objects.get(id=pk)
        except models.Order.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response({"message": "no data"}, status=status.HTTP_204_NO_CONTENT)


class CartListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        carts = models.Cart.objects.all()
        serializer = serializers.CartSerializer(carts, many=True)
        return Response({"carts": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"cart": serializer.data}, status=status.HTTP_201_CREATED)


class CartDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            cart = models.Cart.objects.get(id=pk)
        except models.Cart.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.CartSerializer(cart)
        return Response({"cart": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            cart = models.Cart.objects.get(id=pk)
        except models.Cart.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.CartSerializer(data=request.data, instance=cart)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            cart = models.Cart.objects.get(id=pk)
        except models.Cart.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        cart.delete()
        return Response({"message": "no data"}, status=status.HTTP_204_NO_CONTENT)
