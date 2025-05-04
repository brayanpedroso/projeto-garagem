from rest_framework import viewsets
from core.models import Veiculo
from core.serializers import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
