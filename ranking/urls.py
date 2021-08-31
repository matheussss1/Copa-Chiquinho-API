from django.urls import path
from . import views

urlpatterns = [
    path('ranking/', views.show_ranking, name="ranking"),
]