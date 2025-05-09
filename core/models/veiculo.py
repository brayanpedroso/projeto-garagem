from django.db import models
from core.models import Cor, Acessorio, Modelo

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0) 
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    acessorio = models.ManyToManyField(Acessorio)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id} - {self.modelo} - {self.cor.nome} - {self.ano}"
