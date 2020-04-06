from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import shop.urls
from search import views as search_views
from . import views, ocv
# from .views import notes
from django.views.generic import TemplateView



urlpatterns =  [
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^', include(shop.urls, namespace='shop')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^search/', views.notes, name='search'),
    # Python Social Auth URLs
    url('', include('social.apps.django_app.urls', namespace='social')),
    # Home URL
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    # Logout URL for social Auth
    url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="user-logout"),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^api/',include('socialhand.api.urls',namespace='api')),
    #testing opencv tools into AR
    url(r'^face_detection/camera/$', ocv.camera),
    url(r'^silver_ar/$',views.three.as_view(), name='three'),
    url(r'^honeywell/$',views.Cascade.as_view(), name='cascade'),
    # testing object detect js
    url(r'^glasses/$',views.ben_frank.as_view(), name='ben_frank'),
    url(r'^g876_id0/$',views.ben_frank.as_view(), name='ben_frank'),

    #testing 360 look around  virtual tour with three.js
    url(r'^virtual/$', views.LookAround_360.as_view(), name = 'look_around' ),

     #testing babylon.js
    url(r'^virtual_test_kitchen/$', views.VirtualBabylon.as_view(), name = 'virtual_reality' ),
    url(r'^ar_cr3/$', views.Cr3ationAR.as_view(), name = 'AR_creation' ),
    url(r'^camaro/$', views.CamaroVirtual.as_view(), name = 'camaro' ),
    url(r'^warehouse_test/$', views.Warehouse.as_view(), name = 'warehouse' ),


]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
