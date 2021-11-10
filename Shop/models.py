from django.db import models

# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    image = models.ImageField(upload_to='Categories',
                              null=True, blank=True, verbose_name='Imagen')
    description = models.CharField(max_length=500, verbose_name='Descripción')

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product (models.Model):

    SIZE = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    ]

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoría')
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    description = models.CharField(max_length=500, verbose_name='Descripción')
    image = models.ImageField(upload_to='Products',
                              null=True, blank=True, verbose_name='Imagen')
    price = models.FloatField(verbose_name='Precio')
    size = models.CharField(choices=SIZE, max_length=4,
                            null=True, blank=True, verbose_name='Talla')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['name']

    def __str__(self):
        return self.name
