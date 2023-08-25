from django.db import models
from datetime import datetime 

class Investimento(models.Model):
	Investimento = models.TextField(max_length = 255)
	valor = models.FloatField()
	pago = models.BooleanField(default = false)
	data = models.DateField(default = datetime.now)









































