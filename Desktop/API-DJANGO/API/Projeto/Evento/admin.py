# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Evento)
admin.site.register(Ticket)
admin.site.register(Inscricao)