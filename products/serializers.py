from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes Product instances for API input and output.

    Exposes only the `id` and flexible `fields` payload,
    keeping the API response simple and aligned with the challenge.
    """
    class Meta:
        model = Product
        fields = ['id', 'fields']
