from django.contrib import admin
from django.db import models
from event.models import *

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(Autor)
admin.site.register(ArtigoCientifico)
admin.site.register(CientificoAutor)

