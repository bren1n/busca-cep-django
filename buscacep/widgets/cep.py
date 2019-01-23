from django import forms

class CepWidget(forms.TextInput):
    class Media:
        js = ('js/jquery-3.3.1.min.js', 'js/script-cep.js',)