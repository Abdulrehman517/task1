from django.db import models
from django.db.models import fields
# from rest_framework.fields import ReadOnlyField
from .models import Product, Variant
from rest_framework import serializers


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['title', 'barcode', 'sku']

class ProductSerializer(serializers.ModelSerializer):
    variant = VariantSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'handle', 'body','variant']





    