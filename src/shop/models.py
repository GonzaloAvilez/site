from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta: 
		ordering = ('name',)
		verbose_name = ('category')
		verbose_name_plural = ('categories')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',args=[self.slug])

class Product(models.Model):
	author = models.ForeignKey('authtools.User', null=True)
	category = models.ForeignKey(Category,related_name='products')
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField( upload_to='products/%Y-%m-%d',null=True,blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id, self.slug])

	def save(self, *args, **kwargs):
            try:
                this = Product.objects.get(id=self.id)
                if this.image != self.image:
                    this.image.delete()
            except: pass
            super(Product, self).save(*args, **kwargs)