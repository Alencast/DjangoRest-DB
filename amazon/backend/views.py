from django.shortcuts import render
from rest_framework import viewsets
from .models import Autores, Categorias, Editoras, Emprestimos, Livros, Multas, Reservas, Usuario, LiderEscala, Usuarios
from .serializers import AutoresSerializer, CategoriaSerializer, EditorasSerializer, EmprestimosSerializer, LivrosSerializer, MultasSerializer, ReservasSerializer, UsuarioSerializer, LiderEscalaSerializer, UsuariosSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LiderEscalaViewSet(viewsets.ModelViewSet):
    queryset = LiderEscala.objects.all()
    serializer_class = LiderEscalaSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class EmprestimosViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer

class MultasViewSet(viewsets.ModelViewSet):
    queryset = Multas.objects.all()
    serializer_class = MultasSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

class EditorasViewSet(viewsets.ModelViewSet):
    queryset = Editoras.objects.all()
    serializer_class = EditorasSerializer

