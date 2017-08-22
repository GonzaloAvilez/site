from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
        name='show'),
    url(r'^me/add$', views.post_new, name='post_new_product'),
   	
   	url(r'^profile/(?P<slug>[\w+^\s]+)/$', views.UserProfileView.as_view(), name='profile_view'), 
   	url(r'^profile/id/(?P<pk>\d+)/$', views.UserProfileView.as_view()),
]
