# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=75, verbose_name='Nombre')
	age = models.IntegerField(default=0, verbose_name='Edad')
	phone = models.CharField(max_length=10, verbose_name='Telefono')
	status = models.BooleanField(default=True)

	class Meta:
		db_table='customers'
		#ordering = ['age']
