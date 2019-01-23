from django.shortcuts import render, redirect
from .forms import EnderecoForm
from .models import Endereco

# Create your views here.
def listar(request):
    enderecos = Endereco.objects.all()
    return render(request, 'buscacep/listar.html', {'enderecos': enderecos})

def novo_endereco(request):
    if request.method == "POST":
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_enderecos')
    else:
        form = EnderecoForm()
    return render(request, 'buscacep/novo.html', {'form': form})