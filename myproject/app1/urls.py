
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.customer_list, name='customer_list'),
    url(r'^app/$', views.customer_add, name='customer_add'),
    url(r'^edit/(?P<customer_id>[0-9]+)/$', views.customer_edit, name='customer_edit'),
    url(r'^delete/(?P<customer_id>[0-9]+)/$', views.customer_delete, name='customer_delete'),
]
