from rest_framework import serializers
from .models import Autores, Editoras, Emprestimos, Livros, Multas, Reservas, Usuario, LiderEscala, Usuarios

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class LiderEscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiderEscala
        fields = '__all__'


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros 
        fields = '__all__'

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios 
        fields = '__all__'

class EmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimos 
        fields = '__all__'


class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas 
        fields = '__all__'

class MultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multas
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multas
        fields = '__all__'

class EditorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editoras 
        fields = '__all__'

