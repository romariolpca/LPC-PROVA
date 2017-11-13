# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    admin = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.admin)

class Pessoa(models.Model):
    nome = models.CharField(max_length = 128)
    cpf = models.CharField(max_length = 11)
    user = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return '{}.{}.{}'.format(self.nome, self.cpf, self.user)

class Evento(models.Model):
    nomeEvento = models.CharField(max_length = 128)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    local = models.TextField()

    def __str__(self):
        return '{}.{}.{}.{}'.format(self.nomeEvento, self.dataInicio, self.dataFim, self.local)

class Ticket(models.Model):
    nome = models.CharField(max_length = 128)
    descricao = models.CharField(max_length = 128)
    valor = models.IntegerField()
    idEvento = models.ForeignKey(Evento, null=True, blank=False)

    def __str__(self):
        return '{}.{}.{}.{}'.format(self.nome, self.descricao, self.valor,self.idEvento)

class Inscricao(models.Model):
    idEvento = models.ForeignKey(Evento, null=True, blank=False)
    idPessoa = models.ForeignKey(Pessoa, null=True, blank=False)
    idTicket = models.ForeignKey(Ticket, null=True, blank=False)
    #validacao = models.BooleanField()

    def __str__(self):
        return '{}.{}.{}.{}'.format(self.idEvento, self.idPessoa, self.idTicket)