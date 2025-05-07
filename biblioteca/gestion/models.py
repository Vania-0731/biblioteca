from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, related_name='libros', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name='libros', on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, related_name='prestamos', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    usuario = models.CharField(max_length=200)

    def devolver(self):
        self.fecha_devolucion = models.DateField(auto_now=True)
        self.libro.disponible = True
        self.libro.save()
        self.save()

    def __str__(self):
        return f"{self.libro.titulo} - {self.usuario}"
