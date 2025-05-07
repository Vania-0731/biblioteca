from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libro, Autor, Categoria, Prestamo
from .serializers import LibroSerializer, AutorSerializer, CategoriaSerializer, PrestamoSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

# Endpoint para buscar libros por título, autor o categoría
@api_view(['GET'])
def buscar_libros(request):
    titulo = request.GET.get('titulo', '')
    autor = request.GET.get('autor', '')
    categoria = request.GET.get('categoria', '')
    
    libros = Libro.objects.all()

    if titulo:
        libros = libros.filter(titulo__icontains=titulo)
    if autor:
        libros = libros.filter(autor__nombre__icontains=autor)
    if categoria:
        libros = libros.filter(categoria__nombre__icontains=categoria)

    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)

# Endpoint para registrar préstamos y devoluciones
@api_view(['POST'])
def registrar_prestamo(request):
    libro_id = request.data.get('libro')
    usuario = request.data.get('usuario')
    
    libro = Libro.objects.get(id=libro_id)

    if not libro.disponible:
        return Response({"error": "Libro no disponible"}, status=400)

    prestamo = Prestamo.objects.create(libro=libro, usuario=usuario)
    libro.disponible = False
    libro.save()

    return Response({"mensaje": "Préstamo registrado", "prestamo_id": prestamo.id})

@api_view(['POST'])
def devolver_libro(request):
    prestamo_id = request.data.get('prestamo_id')
    
    prestamo = Prestamo.objects.get(id=prestamo_id)
    prestamo.devolver()

    return Response({"mensaje": "Devolución registrada"})
