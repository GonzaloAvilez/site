# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from .models import Order


"""Celery disbled for prodcution environment inside pythonanywhere
because PA don´t allow to celery works. Then, this isn´t an asynchronous 
task for now"""
# from celery import task
 
# @task
# def order_created(order_id):
# 	"""
# 	Task to send an e-mail notification when an order is
# 	successfully created.
# 	"""
# 	order = Order.objects.get(id=order_id)
# 	subject = 'Orden núm: {}'.format(order.id)
# 	message = 'Estimado {},\n\nHaz realizado tu pedido de manera exitosa.\
# 				Tu número de orden es {}.'.format(order.first_name,
# 											order.id)
# 	mail_sent = send_mail  (subject,
# 							message,
# 							'g.avilez.ig@gmail.com',
# 							[order.email])
	
# 	return mail_sent

def order_created(order_id):
	order = Order.objects.get(id=order_id)
	subject = 'Orden núm: {}'.format(order.id)
	message = 'Estimado {},\n\nHaz realizado tu pedido de manera exitosa.\
				Tu número de orden es {}.'.format(order.first_name,
											order.id)
	mail_sent = send_mail  (subject,
							message,
							'g.avilez.ig@gmail.com',
	 						[order.email])
	return mail_sent

	