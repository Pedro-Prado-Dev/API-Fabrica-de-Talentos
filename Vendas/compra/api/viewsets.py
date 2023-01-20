from rest_framework import viewsets
from compra import models
from compra.api import serializers

class CompraViewSet(viewsets.ModelViewSet):
    queryset = models.Compra.objects.all()
    serializer_class = serializers.CompraSerializer

class CompraViewSetOut(viewsets.ModelViewSet):
    queryset = models.Compra.objects.all()
    serializer_class = serializers.CompraSerializerOut