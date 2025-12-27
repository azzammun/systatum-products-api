from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all products and creating new products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
