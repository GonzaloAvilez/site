#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse
from django.db.models import Q
from authtools.models import User


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Introduce tu Email", autofocus=""),
            Field('password', placeholder="Introduce tu contraseña"),
            Field('remember_me'),

            HTML(""" <div class="text-center no-padding ">
            <ul class="social-network social-circle">  
            <li><a href="{% url 'social:begin' 'facebook' %}" class="icoFacebook ico-background" title="Facebook"><i class="fa fa-facebook"></i></a></li>
            <li><a href="{% url 'social:begin' 'twitter' %}?next={{ request.path }}" class="icoTwitter ico-background" title="Twitter"><i class="fa fa-twitter"></i></a></li>
            <li><a href="{% url 'social:begin' 'google-oauth2' %}" class="icoGoogle ico-background" title="Google +"><i class="fa fa-google-plus"></i></a></li> 
            </ul></div><br> """),

            
            Submit('sign_in', 'Log in',
                   css_class="btn btn-lg btn-primary btn-block"),
            
            HTML('<br><div class="text-right"><a class="text-info" href="{}">Forgot Password?</a></div>'.format(
                reverse("accounts:password-reset"))),

            )



class SignupForm(authtoolsforms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('email', placeholder="Introduce tu Email", autofocus=""),
            Field('name', placeholder="Nombre completo"),
            Field('password1', placeholder="Introduce contraseña"),
            Field('password2', placeholder="Repite tu contraseña"),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )


class PasswordChangeForm(authforms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('old_password', placeholder="Introduce contraseña actual",
                  autofocus=""),
            Field('new_password1', placeholder="Introduce nueva contraseña"),
            Field('new_password2', placeholder="Confirma tu nueva contraseña"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('email', placeholder="Introduce tu email",
                  autofocus=""),
            Submit('pass_reset', 'Reset Password', css_class="btn-warning"),
            )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('new_password1', placeholder="Introduce nueva contraseña",
                  autofocus=""),
            Field('new_password2', placeholder="Confirma tu nueva contraseña"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )
