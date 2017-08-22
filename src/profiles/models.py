# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _
  
 

class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    market = models.CharField(_('Market'), max_length=30, blank=True)
    picture = models.ImageField(_('Profile picture'),
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    background_1 = models.ImageField(_('background_1'),
                                    upload_to = 'profile_background/%Y-%m-%d',
                                    null = True,
                                    blank = True,)
    background_2 = models.ImageField(_('background_2'),
                                    upload_to = 'profile_background/%Y-%m-%d',
                                    null = True,
                                    blank = True,)
    background_3 = models.ImageField(_('background_3'),
                                    upload_to = 'profile_background/%Y-%m-%d',
                                    null = True,
                                    blank = True,)
    fb_link = models.URLField(_('facebook'),
                            validators =[URLValidator()],
                            null=True,
                            blank=True,)
    tw_link = models.URLField(_('Twitter'),
                            validators = [URLValidator()],
                            null=True,
                            blank=True,)
    insta_link=models.URLField(_('instagram'),
                            validators=[URLValidator()],
                            null=True,
                            blank=True,)

    bio = models.CharField(_('Our history'), max_length=400, blank=True, null=True,
        help_text=("Relata un poco sobre tu trabajo: cuánto tiempo llevas haciéndolo, cómo empezó, dónde nació tu creatividad, etc"))

    email_verified = models.BooleanField("Email verificado", default=False)

    class Meta:
        abstract = True

    def get_short_name(self):
        "Devuleve el nombre de la tienda"
        return self.market

@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}' Tienda". format(self.user)


#creating post model for entries.

class Post(models.Model):
    author = models.ForeignKey('authtools.User')
    title = models.CharField(max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    


    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Video(models.Model):
    author= models.ForeignKey('authtools.User')
    title = models.CharField(_('Title'),max_length=200)
    video = EmbedVideoField(
                            help_text='add a valid URL',
                            null=True,
                            blank=True)
    class Meta: 
        ordering = ('title',)
        verbose_name = 'video'
        verbose_name_plural = 'videos'


    def __unicode__(self):
        return self.title


    # def get_absolute_url(self):
    #         return reverse('profiles:detail', kwargs={'pk': self.pk})

        
























