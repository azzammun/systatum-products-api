from django.db import models


class Product(models.Model):
    """
    Represents a product with flexible, JSON-based fields.

    The `fields` attribute allows storing arbitrary product data
    without enforcing a fixed schema.
    """
    # Stores arbitrary product attributes
    fields = models.JSONField()

    # Timestamps for auditing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Human-readable representation for admin/debugging."""
        return f"Product {self.id}"
