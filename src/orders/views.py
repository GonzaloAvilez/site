# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.conf import settings
import weasyprint
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.views import PDFTemplateView




def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()

			for item in cart:
				OrderItem.objects.create(order=order,
										product=item['product'],
										price=item['price'],
										quantity=item['quantity'])

			# clear the cart
			cart.clear()
			#levantar una excepcion si cart esta vacío para informar que
			#no hay productos seleccionados o ya fue generada una orden
			# launch asynchronous task
			#order_created.delay(order.id)
			order_created(order.id)
			request.session['order_id'] = order.id
			return redirect(reverse('payment:process'))

	else:
		form = OrderCreateForm()
	return render(request,
				'orders/order/create.html',
				{'cart': cart, 'form': form})


# decorator to make sure only staff users can access this view for pdf´s
@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request,
				'orders/order/detail.html',
				{'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('orders/order/pdf.html',
							{'order': order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename=\"order_{}.pdf"'.format(order.id)
	stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
	weasyprint.HTML(string=html,
					base_url=request.build_absolute_uri(),
					).write_pdf(response,
								stylesheets=stylesheets)
	return response

class HelloPDFView(PDFTemplateView):
    template_name = "orders/order/pdf.html"


    def get_context_data(self, **kwargs):
    	order_id = self.kwargs.get('order_id')
    	kwargs['order']=get_object_or_404(Order, id=order_id)
        return super(HelloPDFView, self).get_context_data(
            pagesize="b6",
            title="Purchase details",
            **kwargs
        )

