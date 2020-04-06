from django.contrib import admin
from .models import Category, Product, Product3d, Textures3d


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'stock','available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class Product3dAdmin(admin.ModelAdmin):
	list_display = ['mesh_selection','name','slug','custom_model_js']
admin.site.register(Product3d,Product3dAdmin)


class Textures3dAdmin(admin.ModelAdmin):
	list_display = ['model3d','texture_3d']


admin.site.register(Textures3d,Textures3dAdmin)