from rest_framework import serializers
from .models import UsuariosModel


class RegistroSerializer(serializers.Serializer):
    email = serializers.EmailField()
    nombre = serializers.CharField(max_length=50)


class RegistroModelSerializer(serializers.ModelSerializer):
    def save(self):
        # el validated_data es un atributo que se crea cuando se valida el controlador y guardara en un diccionario los datos que se enviaron

        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        password = self.validated_data.get('password')
        is_superuser = self.validated_data.get('is_superuser')

        nuevoUsuario = UsuariosModel(usuarioNombre=usuarioNombre, usuarioCorreo=usuarioCorreo,
                                     usuarioTipo=usuarioTipo, is_superuser=is_superuser)

        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuariosModel
        # definir que vamos a usar todas la columnas
        # fields = '__all__'
        # definir que vamos a usar solo algunas columnas
        # fields = ['usuarioCorreo', 'password']
        # definir que vamos a usar todas las columnas menos algunas
        exclude = ['user_permissions',
                   'groups', 'is_staff', 'last_login', 'is_active']
