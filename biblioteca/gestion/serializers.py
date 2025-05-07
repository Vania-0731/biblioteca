from rest_framework import serializers
from .models import Libro, Autor, Categoria, Prestamo

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Libro
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer()

    class Meta:
        model = Prestamo
        fields = '__all__'
