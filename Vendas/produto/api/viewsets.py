from rest_framework import viewsets
from produto import models
from produto.api import serializers

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)
        marca = self.request.query_params.get('marca', None)
        preco = self.request.query_params.get('preco', None)

        if nome and marca and preco:
            queryset = models.Produto.objects.filter(nome__contains=nome, marca__iexact=marca, preco__lte=preco)
            return queryset

        if nome and marca:
            queryset = models.Produto.objects.filter(nome__contains=nome, marca__iexact=marca)
            return queryset

        if nome and preco:
            queryset = models.Produto.objects.filter(nome__contains=nome, preco__lte=preco)
            return queryset

        if marca and preco:
            queryset = models.Produto.objects.filter( marca__iexact=marca, preco__lte=preco)
            return queryset
        if marca:
            queryset = models.Produto.objects.filter( marca__iexact=marca)
            return queryset
        return models.Produto.objects.all()