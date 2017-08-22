# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.db import models
from shop.models import Product
from django.utils.translation import gettext_lazy as _


 
class Order(models.Model):
	# Contact Details
	first_name = models.CharField(_('First name'),max_length=50)
	last_name = models.CharField(_('Last name'),max_length=50)
	email = models.EmailField(_('E-mail'),)
	formatted_address = models.CharField(_('format Address'), max_length=250, null=True)
	route = models.CharField(_('route'),max_length=100,blank=True,null=True)
	street_number = models.CharField(_('street number'),max_length=20,blank=True,null=True)
	administrative_area_level_1 =  models.CharField(_('state'),max_length=20,blank=True,null=True)
	postal_code = models.CharField(_('postal code'), max_length=20, null=True)
	locality = models.CharField(_('locality'), max_length=100, null=True)
	sublocality = models.CharField(_('sublocality'), max_length=100, null=True)
	country = models.CharField(_('country'), max_length=50, blank=True, null=True)
	country_short = models.CharField(_('country code'),max_length=50, blank=True, null=True)
	created = models.DateTimeField( auto_now_add=True)
	updated = models.DateTimeField( auto_now=True)
	paid = models.BooleanField( default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items',)
	product = models.ForeignKey(Product,related_name='order_items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(_('quantity'),default=1)

	def __str__(self):
		return '{}'.format(self.id)
	def get_cost(self):
		return self.price * self.quantity
