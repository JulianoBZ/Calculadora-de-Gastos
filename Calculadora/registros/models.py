from django.db import models

# Create your models here.

class Transacao(models.Model):
    data = models.DateField(auto_now=True)
    valor = models.DecimalField(decimal_places=2, max_digits= 20)
    tipo = models.IntegerField()

    def __str__(self):
        return "{}, R$ {}, tipo: {}".format(self.data, self.valor, self.tipo)