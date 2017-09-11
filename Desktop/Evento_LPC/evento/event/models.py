from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pessoa(models.Model):
	nome = models.CharField(max_length=124,null=False,blank=False)
	email = models.CharField(max_length=57,null=False,blank=False)
	
	def __str__(self):
		return '{}.{}'.format(self.nome,self.email)


class Evento(models.Model):
	nome = models.CharField(max_length=150, null=True)
	eventoPrincipal = models.CharField(max_length=200, null=True, blank=True)
	sigla = models.CharField(max_length=5,null=True, blank=False)
	dataEHoraDeInicio = models.DateTimeField()
	palavrasChave = models.CharField(max_length=120,null=True) 
	logotipo = models.CharField(max_length=15,null=False)
	realizador = models.ForeignKey(Pessoa,related_name='Eventos',null=True)
	cidade = models.CharField(max_length=45,null=True)
	uf = models.CharField(max_length=2,null=True)
	endereco = models.CharField(max_length=45, null=True,blank=True)
	cep = models.CharField(max_length=12,null=True,blank=False)

	def __str__(self):
		return '{}.{}.{}.{}.{}'.format(self.nome,self.eventoPrincipal,self.sigla,self.uf,self.cep)


class EventoCientifico(Evento):
	issn=models.CharField(max_length=28,null=True)
	
	def __str__(self):
		return '{}'.format(self.issn)


class ArtigoCientifico(models.Model):
	titulo = models.CharField(max_length=130)
	#autores = models.ArrayField()
	autores = models.CharField(max_length=59)
	evento = models.ForeignKey(EventoCientifico,related_name ='ArtigoCientificos',null=True)

	def __str__(self):
		return '{}.{}'.format(self.titulo,self.autores)


class Autor(Pessoa):
	curriculo = models.CharField(max_length=365, null=True,blank=True) 
	artigos = models.CharField(max_length=36, null=True,blank=True) 

	def __str__(self):
		return '{}.{}'.format(self.curriculo,self.artigos)


class PessoaJuridica(Pessoa):
	cnpj = models.CharField(max_length=18, null=True,blank=True) 
	razaoSocial = models.CharField(max_length=80, null=True,blank=True) 

	def __str__(self):
		return '{}.{}'.format(self.cnpj,self.razaoSocial)

class PessoaFisica(Pessoa):
	cpf = models.CharField(max_length=15, null=True,blank=True) 

	def __str__(self):
		return '{}'.format(self.cpf)

class CientificoAutor (models.Model):
	evCientifico = models.ForeignKey(EventoCientifico,null=True)	
	autor = models.ForeignKey(Autor,related_name ='Autor',null=True)
	#evCientifico = models.ManyToManyField(EventoCientifico,Autor)	
	

	def __str__(self):
		return '{}.{}'.format(self.evCientifico,self.autor)
