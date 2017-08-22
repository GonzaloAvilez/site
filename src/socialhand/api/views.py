from rest_framework import generics
from profiles.models import Profile 
from shop.models import Product
from .serializers import ProfileSerializer, ProductSerializer

class ProfileListView(generics.ListAPIView):
	queryset = Profile.objects.all()
	serializer_class =ProfileSerializer

class ProfileDetailView(generics.RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class ProductListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer