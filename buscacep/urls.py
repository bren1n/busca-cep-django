from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('novo', views.novo_endereco, name='novo_endereco')
]
