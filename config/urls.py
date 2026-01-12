
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acconuts/',include('django.contrib.auth.urls')),
    path('acconuts/',include('acconuts.urls')),
    path('', include('blog.urls')),
]
