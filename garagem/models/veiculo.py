from django.db import models
from uploader.models import Image

from garagem.models import Modelo, Acessorio, Cor

class Veiculo(models.Model):
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    descricao = models.CharField(max_length=50, null=True, blank=True)
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"{self.descricao}{self.modelo} {self.ano} ({self.cor})"

    class Meta:
        verbose_name_plural = "veículos"
