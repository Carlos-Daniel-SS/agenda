from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválido !")

    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Eventos.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

def ver_evento(request, titulo_evento):
    evento = Eventos.objects.get(titulo=titulo_evento)
    return HttpResponse(f'<h1>Data do Evento: {evento.data_evento}</h1>')

@login_required(login_url='/login/')
def criar_evento(request):
    id_evento = request.GET.get('id')
    print(id_evento)
    dados = {}
    if id_evento:
        print(id_evento)
        dados['evento'] = get_object_or_404(Eventos, id=id_evento)
        print(dados)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')

        if id_evento:
            evento = Eventos.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = data_evento
                evento.save()
        else:
            Eventos.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Eventos.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')