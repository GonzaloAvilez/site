from django.conf.urls import url
from . import views
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
	url(r'^create/$',views.order_create,name='order_create'),
	url(r'^admin/order/(?P<order_id>\d+)/$',views.admin_order_detail,name='admin_order_detail'),
	url(r'^admin/order/(?P<order_id>\d+)/pdf/$',staff_member_required(views.HelloPDFView.as_view()),name='order_pdf'),
]