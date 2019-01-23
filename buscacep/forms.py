from django import forms
from .models import Endereco
from .widgets.cep import CepWidget

class EnderecoForm(forms.ModelForm):
    cep = forms.CharField(widget=CepWidget)
    
    class Meta:
        model = Endereco
        fields = ('cep', 'localidade', 'logradouro', 'bairro', 'uf')