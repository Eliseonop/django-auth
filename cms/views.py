
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegistroSerializer, RegistroModelSerializer

# Create your views here.


class RegistroController(CreateAPIView):
    serializer_class = RegistroModelSerializer

    def post(self, request):
        print(request.data)
        data = self.serializer_class(data=request.data)
        print(data)
        if data.is_valid():
            nuevoUsuario = data.save()
            resultado = self.serializer_class(instance=nuevoUsuario)
            return Response({'message': 'Usuario registrado correctamente', 'usuario': resultado.data}, status=201)
        else:
            return Response({'errores': data.errors})
