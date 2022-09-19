from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, tipo, password=None):
        """creacion para un usuario normal"""
        if not email:
            raise ValueError('El usuario debe tener un correo')
        # normalizar el correo para que remueva espacios en blanco y ademas valide si cumple con el formato de u ncorreo estandar
        email = self.normalize_email(email)
        # creo mi objeto de usuario Pero todavia no lo guardo en la base de datos
        nuevoUsuario = self.model(
            usuarioCorreo=email, usuarioNombre=nombre, usuarioTipo=tipo)
        # encripto la contraseña
        nuevoUsuario.set_password(password)
        # guardo el usuario en la base de datos
        # self._db esto referencia a la base de datos que se esta utilizando
        nuevoUsuario.save(using=self._db)
        return nuevoUsuario

    """Clase que me sirve para modificar el comportamiento del modelo auth_user en la terminal"""

    def create_superuser(self, usuarioCorreo, usuarioNombre, usuarioTipo, password):
        """Metodo que me permite crear un super usuario"""
        usuario = self.create_user(
            usuarioCorreo, usuarioNombre, usuarioTipo, password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
