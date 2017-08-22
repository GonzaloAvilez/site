from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models
from .models import Post
from shop.models import Category, Product

 
#define user parameter register_registration

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            )

    class Meta:
        model = User
        fields = ['name']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('market'),
            Field('bio'),
            Field('picture'),
            HTML(""" <hr class="basic-custom">"""),
            Field('background_1'),
            HTML("""{% if user.profile.background_1 %}
                        <img class="img-responsive" src="{{ MEDIA_URL }}{{ user.profile.background_1 }}">                
                    {% endif %}
                    <hr class="custom">""", ),                    
            Field('background_2'),
            HTML("""{% if user.profile.background_2 %}
                        <img class="img-responsive" src="{{ MEDIA_URL }}{{ user.profile.background_2 }}">
                    {% endif %}
                    <hr class="custom">""", ),
            Field('background_3'),   
            HTML("""{% if user.profile.background_3 %}
                        <img class="img-responsive" src="{{ MEDIA_URL }}{{ user.profile.background_3 }}">
                    {% endif %}
                    <hr class="custom">""", ),
            Field('fb_link'),
            Field('tw_link'),
            Field('insta_link'),

            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio', 'market','background_1','background_2','background_3','fb_link','tw_link','insta_link',]    


# form for add a new product 
class ShopFor(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(ShopFor, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('category'),
            Field('name'),
            Field('slug'),
            Field('image'),
            Field('description'),
            Field('price'),
            Field('stock'),
            Field('available'),
            Submit('update', 'Update', css_class="btn-success"),
            )


    class Meta:
        model = Product
        fields =['name','slug', 'category', 'image', 'description', 'price','stock', ]


# postform fue agregado para auxiliar la creacion de shopfor 
class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('title','text','author',)
