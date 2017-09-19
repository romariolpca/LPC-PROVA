from django.contrib import admin
from django.db import models
from agen.models import *

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Agenda)
admin.site.register(AgendaPrivada)
admin.site.register(AgendaPublica)
admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(UsuarioAgenda)
admin.site.register(Compromisso)
admin.site.register(Institucional)
