from django.contrib import admin
from django.urls import path, include
from fish_web_service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fish/', include('fish_web_service.urls', namespace='fish_web_service')),
    path('', views.main_page, name='home'),  # Add this line to define the 'home' URL pattern
]

