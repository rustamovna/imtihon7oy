from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartSerializer, CartItemSerializer
from django.utils import timezone



class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))

        cart, created = Cart.objects.get_or_create(user=request.user)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.updated_at = timezone.now()  
        if created:
            cart_item.created_at = timezone.now()  
        cart_item.save()

        return Response({"message": "Mahsulot savatga qo'shildi", 
                         "added_at": cart_item.created_at, 
                         "updated_at": cart_item.updated_at}, status=status.HTTP_201_CREATED)


class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product")
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response({"error": "Savat bo'sh"}, status=status.HTTP_404_NOT_FOUND)

        try:
            item = CartItem.objects.get(cart=cart, product_id=product_id)
            item.delete()
            return Response({"message": "Mahsulot o'chirildi"})
        except CartItem.DoesNotExist:
            return Response({"error": "Mahsulot savatda topilmadi"}, status=status.HTTP_404_NOT_FOUND)


class ClearCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart.items.all().delete()
        return Response({"message": "Savat tozalandi"})


class UpdateCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))
        cart = Cart.objects.filter(user=request.user).first()

        if not cart:
            return Response({"error": "Savat bo'sh"}, status=status.HTTP_404_NOT_FOUND)

        try:
            item = CartItem.objects.get(cart=cart, product_id=product_id)
            item.quantity = quantity
            item.updated_at = timezone.now()  
            item.save()
            return Response({"message": "Mahsulot soni yangilandi", "updated_at": item.updated_at})
        except CartItem.DoesNotExist:
            return Response({"error": "Mahsulot savatda topilmadi"}, status=status.HTTP_404_NOT_FOUND)
