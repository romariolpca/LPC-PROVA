from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pessoa(models.Model):
	nome = models.CharField(max_length=124,null=False,blank=False)
	sexo = models.CharField(max_length=12)
	email = models.CharField(max_length=57,null=False,blank=False)
	endereco = models.CharField(max_length=67)
	
	def __str__(self):
		return '{}.{}.{}.{}'.format(self.nome, self.sexo, self.email,self.endereco)

class Tarefa(models.Model):
	descricaoTar = models.CharField(max_length=89)
	codTarefa = models.CharField(max_length=6)

	def __str__(self):
		return '{}.{}'.format(self.descricaoTar,self.codTarefa)

class Projeto(models.Model):
	nomeP = models.CharField(max_length=365, null=True,blank=True) 
	dataInicio = models.DateTimeField()
	dataFim = models.DateTimeField()
	tarefas = models.ForeignKey(Tarefa,related_name='Tarefas',null=True)
	
	def __str__(self):
		return '{}.{}.{}'.format(self.nomeP,self.dataInicio,self.dataFim)

class Compromisso(models.Model):
	nome = models.CharField(max_length=124,null=False,blank=False)
	dtInicio = models.CharField(max_length=124,null=False,blank=False)
	dtFim = models.CharField(max_length=124,null=False,blank=False)

class Agenda(models.Model):
	nomeAgenda = models.CharField(max_length=124,null=False,blank=False)
	dataAgendamento = models.DateTimeField()
	descricao = models.CharField (max_length=57)
	possuiprojeto = models.ForeignKey(Projeto,related_name='Projetos',null=True)
	

	def __str__(self):
		return '{}.{}.{}'.format(self.nomeAgenda,self.dataAgendamento, self.descricao)


class AgendaPrivada(Agenda):
	codPrivada = models.CharField(max_length=28,null=True)
	
	def __str__(self):
		return '{}'.format(self.codPrivada)


class AgendaPublica(Agenda):
	codPublica = models.CharField(max_length=130)
	
	def __str__(self):
		return '{}'.format(self.codPublica)


class Usuario(Pessoa):
	login = models.CharField(max_length=50, null=True,blank=True) 
	senha = models.CharField(max_length=36, null=True,blank=True) 
	Compromisso = models.ForeignKey(Compromisso,related_name='Comprs',null=True)
	
	def __str__(self):
		return '{}.{}'.format(self.login,self.senha)

class UsuarioAgenda(models.Model):
	usuario = models.ForeignKey(Usuario,related_name='Usuarios',null=True)
	agenda = models.ForeignKey(Agenda,related_name='Agendas',null=True)

class Institucional(models.Model):
	feriadoInstitucional = models.CharField(max_length=50, null=True,blank=True) 
	dataFeriado = models.DateTimeField()
	compromisso = models.ForeignKey(Compromisso,related_name='Compromisso',null=True)
	agenda = models.ForeignKey(Agenda,related_name='Agenda',null=True)
