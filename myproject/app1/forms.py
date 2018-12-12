# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
	name = forms.CharField(
		label = 'Nombre',
		min_length = 3,
		widget = forms.TextInput(
			attrs = {
			}
		)
	)

	age = forms.IntegerField(
		label = 'Edad',
		widget = forms.NumberInput(
			attrs = {
				'required':'required',
				'class':'myclass',
			}
		)
	)

	phone = forms.CharField(
		label = 'Telefono',
		widget = forms.NumberInput(
			attrs = {
			}
		)
	)

	class Meta:
		model = Customer
		fields = ('name', 'age', 'phone',)