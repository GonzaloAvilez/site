from rest_framework import serializers
from profiles.models import Profile
from shop.models import Product

class ProductSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Product
		fields = ('name','author','category','image','description')

class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = ('user','slug', 'market', 'bio', 'picture','password')
        extra_kwargs = {'user':{'lookup_field':'username'}}
