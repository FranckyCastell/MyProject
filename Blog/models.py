from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Blog (models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Título')
    content = models.CharField(max_length=500, verbose_name='Contenido')
    image = models.ImageField(
        upload_to='Blog', null=True, blank=True, verbose_name='Imagen')
    author = models.ForeignKey(
        User, on_delete=CASCADE, verbose_name='Autor', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        ordering = ['title']

    def __str__(self):
        return self.title
