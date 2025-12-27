from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
)

# Product-related API routes
urlpatterns = [
    # List all products or create a new one
    path('', ProductListCreateView.as_view(), name='product-list-create'),

    # Retrieve, update, or delete a specific product by ID
    path('<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),
]
