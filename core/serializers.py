from rest_framework import serializers
from .models import Acessorio, Cor, Modelo, Veiculo


from rest_framework import serializers
from core.models import User  # ou o caminho correto para o modelo User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ou os campos que você deseja expor


class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"

class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
