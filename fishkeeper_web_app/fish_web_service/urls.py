from django.urls import path
from fish_web_service import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('fish/<int:fish_id>/', views.fish_templates, name='fish_id'),
    path('master-classes/', views.master_classes, name='master-classes'),
    path('master-classes/<int:mk_id>/', views.master_classes_templates, name='master-classes-id'),
    path('origami/', views.origami, name='origami'),
    path('search-fish/', views.search_fish, name='search-fish'),
    path('registration/', views.registration, name='registration'),
    path('add-fish/', views.add_fishes, name='add_fish'),
    path('search-master-classes/', views.search_master_classes, name='search_mk'),
    path('programming/', views.programming, name='programming'),
]

handler404 = views.page_not_found
