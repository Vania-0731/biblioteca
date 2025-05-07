from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet, CategoriaViewSet, PrestamoViewSet, buscar_libros, registrar_prestamo, devolver_libro, listar_libros_disponibles

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('buscar_libros/', buscar_libros, name='buscar_libros'),
    path('registrar_prestamo/', registrar_prestamo, name='registrar_prestamo'),
    path('devolver_libro/', devolver_libro, name='devolver_libro'),
    path('libros_disponibles/', listar_libros_disponibles, name='libros_disponibles'),
    path('', include(router.urls)),
]
