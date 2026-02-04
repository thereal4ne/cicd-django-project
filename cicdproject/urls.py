from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webapp.urls')),  # <-- ADD THIS LINE
    path('admin/', admin.site.urls),
]
