# evento/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Evento

class EventoDetailView(DetailView):
    model = Evento
    template_name = 'evento/detalle_evento.html'
    context_object_name = 'evento'
