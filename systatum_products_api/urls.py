from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),

    # Products API endpoints
    path('products/', include('products.urls')),

    # Redirect root URL to the products API for convenience
    path("", RedirectView.as_view(url="/products/", permanent=False)),
]
