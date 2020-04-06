from __future__ import unicode_literals
from django import forms
from .models import Product3d
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Button, HTML, Row, Field, Fieldset

class Custom3dForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super(Custom3dForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            Field('custom_model_js'),
            # Submit('submit','Save Code', ccss_class='btn btn-success')
            # Submit('update', 'Update', css_class="btn-success"),
            Submit('update','Save Code',css_class="btn-success"),
            )

    class Meta:
        model = Product3d
        fields = ['custom_model_js','texture3d']
