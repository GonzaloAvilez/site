# coding: utf-8
from django import forms 
from crispy_forms.helper import FormHelper                                                
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import InlineField


# class ContactForm(forms.Form):
#   subject = forms.CharField (label='Asunto', required = False,)
#   contact_name = forms.CharField(required=True,
#                               label='Your Name')
#   contact_email = forms.EmailField(required=True,
#                               label='Your Email')
#   content = forms.CharField (required=True,
#                               widget=forms.Textarea,
#                               label='Your Message')

#   def __init__(self, *args,**kwargs):
#       super(ContactForm, self).__init__(*args, **kwargs)
#       self.helper = FormHelper ()
#       # self.helper.form_class = 'form-inline'
#       # self.helper.laber_class = 'col-lg-2'
#       # self.helper.field_class = 'col-lg-8'
#       self.helper.layout=Layout(
#               # Div(  
#               #   InlineField('contact_name'), 
#               #   InlineField('contact_email'),
#               #   InlineField('subject'),
#               #   InlineField('content'),
#               #   ),
                
#               Div(
#                   InlineField('subject', css_class='form-control custom-placeholder input-contact input-lg'), 
#                   InlineField('contact_email',css_class='form-control input-contact custom-placeholder input-lg'),
#                   InlineField('contact_email',css_class='form-control input-contact custom-placeholder input-lg'),
#                   InlineField('contact_name',css_class='form-control input-contact custom-placeholder input-lg'), 
#                   css_class="col-lg-6 form-group lead",
                        
#                   ),
#               Div(
#                   InlineField('content', css_class='input-contact'),
#                   css_class="col-lg-6 form-group",
#                   ),
                
#           Submit('submit', 'Send Message',css_class="btn btn-contact btn-default"),
                    
#           )


class ContactForm(forms.Form):
    subject = forms.CharField(
                        label='Asunto',
                        required=False
                    )
    name = forms.CharField(
                        label='Nombre',
                        required=False
                    )
    email = forms.EmailField(
                        label='Correo electrónico',
                        required=False
                    )
    content = forms.CharField(
                        label="Contenido",
                        widget=forms.Textarea,
                        required=False,
                    )

    widgets = {
        'subject': forms.TextInput(
            attrs={
                'placeholder': 'Asunto a tratar'
                }
            ),
        'name': forms.TextInput(
            attrs={
                'placeholder': 'Escribe tu nombre completo'
                }
            ),
        'email': forms.TextInput(
            attrs={
                'placeholder': 'Escribe tu email'
                }
            ),
        'content': forms.TextInput(
            attrs={
                'placeholder': 'Cuéntanos cómo podemos ayudarte'
                }
            )
    }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control custom-placeholder',
                # TODO required is used for styling;cleaned_data not working here
                'required': 'required'
                })

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if not subject:
            raise forms.ValidationError(u'Sobre qué tema quieres contarnos')
        return subject

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError(u'Ingresa tu nombre completo')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError(u'Ingresa tu email')
        return email

    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            raise forms.ValidationError(u'Cuáles son tus inquietudes')
        return content
