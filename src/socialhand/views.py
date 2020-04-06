from django.views import generic
from django.shortcuts import render,render_to_response,redirect
from .forms import ContactForm
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
# Elasticsearch
# from .forms import PostSearchForm


class HomePage(generic.TemplateView):
    template_name = "home.html"
    http_method_names = ['get', 'post']


    def get(self,request,*args,**kwargs):
    	form_class = ContactForm


    	kwargs['form'] = form_class
    	return super(HomePage,self).get(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
    	form_class = ContactForm
    	kwargs['form'] = form_class
    	if request.method == 'POST':
    		form = form_class(data=request.POST)
	    	if form.is_valid():
	    		subject = request.POST.get('subject','')
	    		contact_name = request.POST.get('contact_name','')
	    		contact_email = request.POST.get('contact_email','')
	    		content = request.POST.get('content','')
	    		template = get_template('contact_template.txt')
	    		context = Context({
	    			'subject':subject,
	    			'contact_name':contact_name,
	    			'contact_email':contact_email,
	    			'content':content,
	    			})
	    		content = template.render(context)
	    		email = EmailMessage(
	    			"New contact form submission",
	    			content,
	    			"from@example.com"+'',
	    			['g_avilez_ig@hotmail.com'],
	    			headers = {'Reply to':contact_email})
	    		email.send()
	    		# return redirect('get')
    	return super(HomePage,self).get(request,*args,**kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def contact(request):
	form_class= ContactForm
	return render(request,"contact.html",{'form':form_class},)

# Generic view for Augmented reality
class three(generic.TemplateView):
    template_name = "three.html"

class Cascade(generic.TemplateView):
    template_name = "cascade.html"

class ben_frank(generic.TemplateView):
    template_name = "glasses.html"

#generic view for 360 look around
class LookAround_360(generic.TemplateView):
    template_name = "360_virtualtour.html"

class VirtualBabylon(generic.TemplateView):
    template_name = "babylon.html"

class Cr3ationAR(generic.TemplateView):
    template_name = "ar_cr3ation.html"

class CamaroVirtual(generic.TemplateView):
    template_name = "camaro_virtual.html"

class Warehouse(generic.TemplateView):
    template_name = "warehouse_babylonjs.html"






#view for elasticsearch
# def notes(request):
#     form = PostSearchForm(request.GET)
#     posts = form.search()
#     return render_to_response('notes.html', {'posts': posts})


