from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models  import *
from .serializer  import *

class PatraoViewSet(viewsets.ModelViewSet):
    queryset = Patrao.objects.all()
    serializer_class = PatraoSerializer

class ConfiguraViewSet(viewsets.ModelViewSet):
    queryset = Configura.objects.all()
    serializer_class = ConfiguraSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class JustificativaViewSet(viewsets.ModelViewSet):
    queryset = Justificativa.objects.all()
    serializer_class = JustificativaSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer