# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, Http404

from .forms import CustomerForm
from .models import Customer

# Create your views here.
def customer_list(request):
	customers = Customer.objects.filter(status=True)
	return render(request, 'app1/customer_list.html', {'customers':customers})

def customer_add(request):

	cust_form = CustomerForm()

	cust_form = CustomerForm(request.POST or None)

	if cust_form.is_valid():

		cust_form.save()

		return redirect('app:customer_list')

	return render(request, 'app1/customer_form.html', {'form':cust_form})

def customer_edit(request, customer_id):
	customer = Customer.objects.get(pk=customer_id)

	cust_form = CustomerForm(request.POST or None, instance=customer)

	if cust_form.is_valid():

		cust_form.save()

		return redirect('app:customer_list')

	return render(request, 'app1/customer_form.html', {'form':cust_form})

def customer_delete(request, customer_id):
	
	try:
		customer = Customer.objects.get(pk=customer_id)
		customer.status = False
		customer.save()
	except Exception as e:
		raise Http404

	return redirect('app:customer_list')

