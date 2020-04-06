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

# function will be loaded only in Product3d class
def get_upload_path(instance, filename):
		""" apliying rsplit(condition,counter) :delete last elements from right to left
		and getting element by indexing selection []>>left to right  from ({././.},{.json})"""
		# Removing last slash from storage3d.URL: ("/media/models3d/<Date>","model_name.json")
		path_instance = instance.storage3d.url.rsplit('/',1)[0]
		""" apliying split(condition,counter) and removing firts elements from left to right
		and getting element by indexing selection [-1]>>right to left from ({././},{models3d/<Date>})"""
		# Removing first and second one slashes and getting last element
		path_dirname = path_instance.split('/',2)[-1]
		# join and build path to save model instance when function is loaded
		return '/'.join ([path_dirname, filename])


class Product3d(models.Model):
    mesh_selection = models.ForeignKey(Product, related_name='mesh', null=True)
    slug = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    storage3d = models.FileField(upload_to='models3d/%Y-%m-%d', null=True, blank=True)
    texture3d = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    custom_model_js = models.FileField(upload_to='models3d/each-js', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('shop:product_rendering', args=[self.id, self.slug])

    def __str__(self):
        return self.name



storage3d_upload_to = Product3d._meta.get_field('storage3d').upload_to
class Textures3d(models.Model):
    model3d = models.ForeignKey(Product3d)
    texture_3d = models.ImageField(upload_to=storage3d_upload_to,null=True,blank=True)


    def __str__(self):
        return self.name




