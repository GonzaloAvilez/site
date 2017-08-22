from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from authtools.models import User
from profiles.views import ShowProfile

from shop.models import Category, Product
from profiles.models import Profile

# Create your views here.


def search(request):
	if 'q' in request.GET:
		querystring = request.GET.get('q').strip()
		if len(querystring) == 0:
			return redirect ('/search/')
		try:
			search_type = request.GET.get('type')
			if search_type not in ['products','categories','profiles']:
				search_type = 'products'
		except Exception, e:
			search_type = 'products'

		count = {}
		results = {}
		
		results['products'] = Product.objects.filter(Q(name__icontains=querystring) | Q(description__icontains=querystring) | Q(slug__icontains=querystring))
		results['categories'] = Category.objects.filter(name__icontains=querystring)
		results['profiles'] = Profile.objects.filter(Q(market__icontains=querystring) | Q(bio__icontains=querystring) | Q(user__name__icontains=querystring))


		count['products'] = results['products'].count()
		count['categories'] = results['categories'].count()
		count['profiles'] = results['profiles'].count()


		return render(request,'search/results.html',{'hide_search':True,
													'querystring':querystring,
													'active':search_type,
													'count':count,
													'results':results[search_type]})
	else:
		return render(request,'search/search.html',{'hide_search':True})