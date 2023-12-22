from django.db import models
from django.contrib.auth.models import User


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
