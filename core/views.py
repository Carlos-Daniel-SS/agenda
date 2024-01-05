from django.shortcuts import render, HttpResponse, redirect
from .models import Eventos


# Create your views here.

def ver_evento(request, titulo_evento):
    evento = Eventos.objects.get(titulo=titulo_evento)
    return HttpResponse(f'<h1>Data do Evento: {evento.data_evento}</h1>')

def lista_eventos(request):
    evento = Eventos.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

#def index(request):
 #   return redirect('/agenda/')