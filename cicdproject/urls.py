from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webapp.urls')),   # root URL
    path('admin/', admin.site.urls),
]
