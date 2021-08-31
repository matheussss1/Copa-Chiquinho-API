from django.urls import path
from . import views

urlpatterns = [
    path('ranking/', views.show_ranking, name="ranking"),
    # path(r'upload/<str:player>/<str:filename>/', views.show_image, name="player_image"),
]