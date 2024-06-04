from django.contrib import admin
from contatos.models import Contato


# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')
    list_display_links = ('id', 'nome')
    search_fields= ('id', 'nome')
admin.site.register(Contato, ContatoAdmin)