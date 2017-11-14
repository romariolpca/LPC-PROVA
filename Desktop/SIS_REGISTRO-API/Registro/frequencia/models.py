from django.db import models
# Create your models here.

class Patrao(models.Model):
	nome = models.CharField(max_length=145)
	depart = models.CharField(max_length=145)

def __str__(self):
	return '{}.{}.'.format(self.nome,self.depart)

class Configura(models.Model):
	hs_entrada = models.DateField()
	hs_saida = models.DateField()
	hs_trab_dia = models.DateField()
	
	def __str__(self):
    	    return '{}.{}.{}'.format(self.hs_entrada,self.hs_saida,self.hs_trab_dia)

class Funcionario(models.Model):
    nomefun = models.CharField(max_length=145)
    funcao = models.CharField(max_length=145)
    cpf = models.CharField(max_length=145)
    cargo = models.CharField(max_length=145)
    departamento = models.CharField(max_length=145)
    conf = models.ForeignKey(Configura,null=True, blank=False)
    
    def __str__(self):
        return '{}.{}.{}.{}.{}'.format(self.nomefun,self.funcao,self.cpf,self.cargo,self.departamento,self.conf)

 
class Frequencia (models.Model):
	tipo_registro = models.CharField(max_length=145)
	horario_reg = models.DateField()
	ip_maquina = models.CharField(max_length=145)
	status = models.CharField(max_length=145)
	chef = models.ForeignKey(Patrao, null=True, blank=False)
	
	def __str__(self):
		return '{}.{}.{}.{}.{}'.format(self.tipo_registro,self.horario_reg,self.ip_maquina,self.status,self.ip_maquina)

class Justificativa(models.Model):
	descricao = models.TextField(blank=True,null=True)
	chefe = models.ForeignKey(Patrao, null=True, blank=False)
	frequencia = models.ForeignKey(Frequencia, null=True, blank=False)


	def __str__(self):
    	    return '{}.{}.{}'.format(self.descricao,self.chefe,self.frequencia)
