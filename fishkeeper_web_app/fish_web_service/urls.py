from django.urls import path
from . import views

app_name = 'fish_web_service'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('fish/<int:pk>/', views.fish_detail, name='fish_detail'),
    path('add_fish/', views.add_fish, name='add_fish'),
    path('search/', views.search_fish, name='search_fish'),
    path('registration/', views.registration, name='registration'),
    path('master_classes/', views.master_classes, name='master_classes'),
    path('origami/', views.origami, name='origami'),
    path('master_classes_templates/<int:mk_id>/', views.master_classes_templates, name='master_classes_templates'),
    path('fish_templates/<int:fish_id>/', views.fish_templates, name='fish_templates'),
    path('none_indexed/', views.NONE_indexed, name='none_indexed'),
]
