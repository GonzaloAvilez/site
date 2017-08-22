from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^profiles/$',views.ProfileListView.as_view(),),
	url(r'^profiles/(?P<pk>\d+)/$',views.ProfileDetailView.as_view(),name='profile_detail'),
	url(r'^products/$',views.ProductListView.as_view(),),

]