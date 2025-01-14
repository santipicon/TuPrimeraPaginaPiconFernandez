from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="posts")  # Relación con el autor
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
