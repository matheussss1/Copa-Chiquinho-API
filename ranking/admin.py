from django.contrib import admin

from .models import Jogador
# Register your models here.
@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'idade', 'status', 'esta_devendo', 'observacoes')