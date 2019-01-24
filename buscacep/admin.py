from django.contrib import admin
from .models import Endereco, Cidade
from .forms import EnderecoForm

# Register your models here.
class EnderecoAdmin(admin.ModelAdmin):
    form = EnderecoForm
    # class Media:
    #     js = ('js/jquery-3.3.1.min.js', 'js/script-cep.js',)

admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Cidade)