from django.shortcuts import render, HttpResponse
from .models import Eventos


# Create your views here.

def ver_evento(request, titulo_evento):
    evento = Eventos.objects.get(titulo=titulo_evento)
    return HttpResponse(f'<h1>Data do Evento: {evento.data_evento}</h1>')
