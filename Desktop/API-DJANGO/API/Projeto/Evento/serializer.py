from rest_framework import routers, serializers, viewsets
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('admin',)

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer
    class Meta:
        model = Pessoa
        fields = ('nome','cpf','user')

    def create(self, dados):
        print(dados)
        pessoa = Pessoa.objects.get(**dados)
        return Ticket.objects.create(self,**dados)

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento 
        fields = ('nomeEvento','dataInicio', 'dataFim', 'local')
    
    def create(self, validate_data):
        return Evento.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.nomeEvento = validate_data.get('nomeEvento', instance.nomeEvento)
        instance.dataInicio = validate_data.get('dataInicio', instance.dataInicio)
        instance.dataFim = validate_data.get('dataFim', instance.dataFim)
        instance.local = validate_data.get('local', instance.local)
        instance.save()
        return instance


    '''
    def create (self, validate_data):
        dados_User = dados.pop('usuario')
        u = User.objects.create(**dados_User)
        p = Evento.objects.create(usuario=u,**dados)
        return p
        #return Comment.objects.create(**validate_data)
    '''

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    idEvento = EventoSerializer(many=False)
    class Meta:
        model = Ticket
        fields = ('nome','descricao','valor','idEvento')

    def create(self, dados):
        print(dados)
        e = dados.pop("idEvento")
        eventos = Evento.objects.get(**e)
        return Ticket.objects.create(idEvento=eventos,**dados)

class InscricaoSerializer(serializers.HyperlinkedModelSerializer):
    idEvento = EventoSerializer
    idPessoa = PessoaSerializer
    idTicket = TicketSerializer
    
    class Meta:
        model = Inscricao
        fields = ('idEvento','idPessoa','idTicket')

    def create(self, dados):
        print(dados)
        e = dados.pop("idEvento")
        eventos = Evento.objects.get(**e)
        return Ticket.objects.create(idEvento=eventos,**dados)