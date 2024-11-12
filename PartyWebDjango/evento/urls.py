# evento/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.EventoDetailView.as_view(), name='detalle_evento'),
]
