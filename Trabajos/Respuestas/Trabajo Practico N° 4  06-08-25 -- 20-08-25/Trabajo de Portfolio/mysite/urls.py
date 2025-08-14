from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Portfolio.urls')),
    path('portfolio/', include('Portfolio.urls')),
    path('blog/', include('Blog.urls')),
]
