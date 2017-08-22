from __future__ import unicode_literals

from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

class PaymentConfig(AppConfig):
	name = 'payment'
	verbose_name = 'Payment'

	def ready(self):
		# import signal handlers
		import payment.signals