from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import  ProductListView

urlpatterns = [
 
	url(r'^productos/$', ProductListView.as_view(), name='product_list'),
	url(r'^productos/(?P<slug>[-\w]+)/$',ProductListView.as_view(),name='product_list_by_category'),
	url(r'^productos/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
	url(r'^productos/(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', views.product_edit, name='product_edit'),
	url(r'^productos/(?P<id>\d+)/(?P<slug>[-\w]+)/remove/$',views.product_remove, name='product_remove'),
	url(r'^ranking/$', views.product_ranking, name='create'),
	# paginacion alternativa no definitiva
	url(r'^auto/$', ProductListView.as_view()),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


