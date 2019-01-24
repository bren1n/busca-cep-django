from django import forms
from .models import Endereco, Cidade
from .widgets.cep import CepWidget

class EnderecoForm(forms.ModelForm):
    cep = forms.CharField(widget=CepWidget)
    localidade = forms.ModelChoiceField(queryset=Cidade.objects.all(),to_field_name="nome")
    
    class Meta:
        model = Endereco
        fields = ('cep', 'localidade', 'logradouro', 'bairro', 'uf')