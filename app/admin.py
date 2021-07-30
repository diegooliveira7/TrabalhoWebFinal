
from django.contrib import admin
from .models import *

class EstudantesAdmin(admin.ModelAdmin):
    list_display = ('nome','ingresso')

admin.site.register(Estudantes, EstudantesAdmin)


