from django import forms 
from crispy_forms.helper import FormHelper                                                
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import InlineField

class ContactForm(forms.Form):
	subject = forms.CharField (required = False,)
	contact_name = forms.CharField(required=True,
								label='Your Name')
	contact_email = forms.EmailField(required=True,
								label='Your Email')
	content = forms.CharField (required=True,
								widget=forms.Textarea,
								label='Your Message')

	def __init__(self, *args,**kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper ()
		# self.helper.form_class = 'form-inline'
		# self.helper.laber_class = 'col-lg-2'
		# self.helper.field_class = 'col-lg-8'
		self.helper.layout=Layout(
				
				# Div(	
				# 	InlineField('contact_name'), 
				# 	InlineField('contact_email'),
				# 	InlineField('subject'),
				# 	InlineField('content'),
				# 	),
				
				Div(
					InlineField('subject',css_class='form-control input-contact input-lg'), 
					InlineField('contact_email',css_class='form-control input-contact input-lg'),
					InlineField('contact_name',css_class='form-control input-contact input-lg'),	
					css_class="col-lg-6 form-group lead",
						
					),
				Div(
					InlineField('content', css_class='input-contact'),
					css_class="col-lg-6 form-group",
					),
				
			Submit('submit', 'Send Message',css_class="btn btn-contact btn-default"),
					
			)
