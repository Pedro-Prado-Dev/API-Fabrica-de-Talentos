from rest_framework import viewsets
from cliente import models
from cliente.api import serializers


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()

    def get_queryset(self):
        cpf = self.request.query_params.get('id', None)
        if cpf == None:
            queryset = models.Cliente.objects.filter()
        else:
            queryset = models.Cliente.objects.filter(cpf=cpf)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
