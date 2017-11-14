from rest_framework import routers, serializers, viewsets
from .models import *


class PatraoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrao
        fields = ('nome','departamento')

    def create(self, dados):
        return Patrao.objects.create(**dados)


class ConfiguraSerializer(serializers.HyperlinkedModelSerializer):
    conf = ConfiguraSerializer
    class Meta:
        model = Configura
        fields = ('hs_entrada','hs_saida','hs_trab_dia','conf')

    def create(self, dados):
        return Configura.objects.create(**dados)
	
class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
    chef = PatraoSerializer
    class Meta:
        model = Frequencia
        fields = ('tipo_registro','horario_reg','ip_maquina','status','chef')

    def create(self, dados):
        return Frequencia.objects.create(**dados)

class JustificativaSerializer(serializers.HyperlinkedModelSerializer):
    idchefe = PatraoSerializer
    idFreque = FrequenciaSerializer
    
    class Meta:
        model = Justificativa
        fields = ('descricao','chefe','frequencia')

     def create(self, dad):
        return Justifica.objects.create(**dad)


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    conf = ConfiguraSerializer(many=False)
    class Meta:
        model = Funcionario
        fields = ('nomefun','funcao','cpf','cargo','departamento','conf')

     def create(self, dados):
        return Funcionario.objects.create(**dados)