from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Panel de administración
    path('', include('portfolio.urls')),      # Página principal -> portfolio
    path('blog/', include('blog.urls')),      # Rutas del blog
]
