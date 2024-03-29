from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Eventos(models.Model):

    titulo = models.CharField(verbose_name='Titulo do Evento', max_length=100)
    descricao = models.TextField(verbose_name='Descrição do Evento', blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return (f'Titulo: {self.titulo}| Descrição: {self.descricao}| Data do evento: {self.data_evento}| Data de '
                f'criação: {self.data_criacao}')

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        return False
    def get_condicao_evento(self):
        diferenca = self.data_evento - datetime.now()
        return diferenca.seconds/60/60 <= 1

