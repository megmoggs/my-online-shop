from django.conf.urls import url 
from . import views

urlpatterns =  [
	url(r'^$', views.product_listing, name='product_listing')
	]