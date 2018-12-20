from django.db import models

class Pen(models.Model):
	pen_name = models.CharField(max_length=200)
	pen_price = models.CharField(max_length=10)

