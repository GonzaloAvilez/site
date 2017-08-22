from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

 
 
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 40)]
class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(
								choices=PRODUCT_QUANTITY_CHOICES,
								coerce=int,
								label='')
	update = forms.BooleanField(required=False,
								initial=False,
								widget=forms.HiddenInput) 
	def __init__ (self,*args, **kwargs):
		super (CartAddProductForm,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.form_tag = False
		self.helper.layout = Layout (
			Field ('quantity'),
			Field ('update'),
			Submit('update', 'Add to cart', css_class='btn-success')

			)