from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TipoAgenda(models.Model):
	nome = models.CharField(max_length=124,null=False,blank=False)

	def __str__(self):
			return '{}'.format(self.nome)

class Agenda(models.Model):
	nomeAgenda = models.CharField(max_length=124,null=False,blank=False)
	dataAgendamento = models.DateTimeField()
	descricao = models.CharField (max_length=57)
	tipoagend = models.ForeignKey(TipoAgenda,related_name='TipoAgendas',null=True)
	
	def __str__(self):
		return '{}.{}.{}'.format(self.nomeAgenda,self.dataAgendamento, self.descricao)

class UsuarioAgenda(models.Model):
	usuario = models.ForeignKey(User,related_name='Usuarios',null=True)
	agen = models.ForeignKey(Agenda,related_name='Agendas',null=True)

	def __str__(self):
			return '{}.{}.{}'.format(self.usuario,self.agenda)

class Compromisso(models.Model):
	nome = models.CharField(max_length=124,null=False,blank=False)
	dtInicio = models.DateTimeField()
	dtFim = models.DateTimeField()
#	agenda = models.ForeignKey(Agenda,related_name='Agendas',null=True)

	def __str__(self):
			return '{}.{}.{}'.format(self.nome,self.dtInicio, self.dtFim)

class Convite (models.Model):

	descricaoCompromisso = models.CharField(max_length=124,null=False,blank=False)
	confirmarouDeclinar = models.CharField(max_length=124,null=False,blank=False)
	usercom = models.ForeignKey(User,related_name='users',null=True)
	compromisso = models.ForeignKey(Compromisso,related_name='Compromisses',null=True)