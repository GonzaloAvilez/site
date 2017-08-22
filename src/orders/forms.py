#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

  
class OrderCreateForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(OrderCreateForm,self).__init__ (*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class  = 'col-lg-9'
		self.helper.layout = Layout (
				
				Div(HTML("<h2 class='text-center'>Shipping details</h2>")	,
					InlineField('formatted_address', required=True, css_class="container-fluid"),		
					# Field('route', required=False, css_class="order-form"),
					# Field('street_number', required=False, css_class="order-form"),
					# Field('sublocality', required=True, css_class="order-form"),
					# Field('locality', required=True, css_class="order-form"),
					# Field('postal_code', required=True, css_class="order-form"),
					Div(
                		Div('route', css_class="col-sm-6 col-xs-6 order-form-padding"),
                		Div('street_number', css_class="col-sm-6 col-xs-6 order-form-padding"),
                		css_class = 'row'
            			),
					Div(
                		Div('sublocality', css_class="col-sm-6 col-xs-6 order-form-padding"),
                		Div('postal_code', css_class="col-sm-6 col-xs-6 order-form-padding"),
                		css_class = 'row'
            			),
					Div(
                		Div('locality', css_class="col-sm-6 col-xs-6 order-form-padding order-form"),
                		Div('administrative_area_level_1', css_class="col-sm-6 col-xs-6 order-form-padding order-form"),
                		css_class = 'row'
            			),
					Div(
                		Div('country', css_class="col-sm-6 col-xs-6 order-form-padding order-form"),
                		Div('country_short', css_class="col-sm-6 col-xs-6 order-form-padding order-form"),
                		css_class = 'row'
            			),
					# Field('administrative_area_level_1', required=False, css_class="order-form"),
					# Field('country', required=False, css_class="order-form"),
					# Field('country_short', required=False, css_class="order-form"),
					css_class="col-lg-6 ",
					),
				Div(HTML("<h2 class='text-center'>Contact details</h2>"),
					Field('first_name', required=False, css_class="order-form"),
					Field('last_name', required=False, css_class="order-form"),
					Field('email', required=False, css_class="order-form"),
					css_class="col-lg-6",
				),)
	
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email',
				'postal_code', 'locality', 'sublocality',
				'country_short','country', 'route',
				'formatted_address','street_number', 
				'administrative_area_level_1',]