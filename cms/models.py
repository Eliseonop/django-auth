from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from .authManager import UsuarioManager


class ProductosModel(models.Model):
    productoId = models.AutoField(
        primary_key=True,
        null=False,
        db_column='id',
        unique=True,
    )
    productoNombre = models.CharField(
        max_length=50,
        null=False,
        db_column='nombre',
    )
    productoPrecio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        db_column='precio',
    )

    class Meta:
        db_table = 'productos'
        ordering = ['-productoPrecio']


class UsuariosModel(AbstractBaseUser, PermissionsMixin):
    """Este modelo es un modelo que modificara la creacion de la tabla Auth User que viene por defecto dentro de todos los proyectos de Django"""
    TIPO_USUARIO = [
        (1, 'ADMIN'),
        (2, 'CLIENTE'),
        (3, 'VENDEDOR'),
    ]

    usuarioId = models.AutoField(
        db_column='id',
        primary_key=True,
        unique=True,
    )

    usuarioNombre = models.CharField(
        max_length=50,
        db_column='nombre',
        null=False,
    )

    usuarioCorreo = models.EmailField(
        db_column='correo',
        null=False,
        unique=True,
        verbose_name='Correo',
    )

    usuarioTipo = models.IntegerField(
        db_column='tipo_usuario',
        choices=TIPO_USUARIO,
        default=2,
    )

    password = models.TextField(
        # db_column='password',
        # null=False,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # comportamiendo del modelo al momento de crear un superuser por consola o terminal
    objects = UsuarioManager()

    # ahora defino la columna que sera la encargada de validar que el usuario sea unico
    USERNAME_FIELD = 'usuarioCorreo'

    # Sirve apra indicar que campos van a ser  solicitados al momento de crear el super usuario en la terminal
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioTipo']

    class Meta:
        db_table = 'usuarios'
