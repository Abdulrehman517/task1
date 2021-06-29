from django.shortcuts import render
from .models import Product, Variant

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import ProductSerializer, VariantSerializer
from .models import Product, Variant
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status


class ProductList(APIView):
    def get(self, request, format=None):
        products= Product.objects.all()
        serializer  = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductVariant(APIView):
    def get(self, request, format=None):
        variants= Variant.objects.all()
        serializer  = VariantSerializer(variants, many=True)
        return Response(serializer.data)



