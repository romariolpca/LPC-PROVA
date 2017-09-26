from django.shortcuts import render
#from django.http import HttpResponse
#from agen.models import Agenda
#from agen.models import AgendaPublica
#from agen.models import Institucional

# Create your views here.
#def agendascadastradas(request):
#	retorno = "<h1>Agendas Cadastradas <h1>"
#	cadastradas = Agenda.objects.all()
#	for agen in cadastradas:
#		retorno +='</br>Lista das Agendas Cadastradas: {}</br>'.format(agen.nomeAgenda)
#	return HttpResponse(retorno)

#def publica():
#	retorno = "<h1>Agendas Pública<h1>"
#	cadastradas = AgendaPublica.gets(codPublica=PUB985)
#	for agen in cadastradas:
#		retorno +='</br>Lista das Agendas Cadastradas: {}</br>'.format(agen.nomeAgenda)
#	return HttpResponse(retorno)

#def feriados(request):
#	retorno = "<h1>Feriados <h1>"
#	feriadosinst = Institucional.objects.all()
#	for agen in feriadosinst:
#		retorno +='</br>Lista das Agendas Cadastradas: {}</br>'.format(agen.feriadoInstitucional)
#	return HttpResponse(retorno)

