from django.db import models

# Create your models here.
class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=False)
    descripcion = models.TextField()

    class Meta:
        db_table = 'platos'
        # sirve para modificar el ordenamiento predeterminado de la BD
        # 'nombre'  > ordenara de A a Z
        # '-nombre' > ordenara de Z a A
        ordering = ['nombre']