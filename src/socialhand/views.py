# coding: utf-8
from django.views import generic
from django.shortcuts import render,render_to_response,redirect
from .forms import ContactForm
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
# Elasticsearch
# from .forms import PostSearchForm
from django.contrib import messages

class HomePageView(generic.FormView):
	template_name = "home.html"
	form_class = ContactForm
	success_url = 'home'

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		return context

	def form_valid(self, form):
		form.save()
		messages.success(self.request, "Envío Exitoso")
		return super(ProspectView, self).form_valid(form)




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
    	context = Context({})
    	if request.method == 'POST':
    		form = form_class(data=request.POST)
    		print form['subject'].value()
	    	if form.is_valid():
	    		subject = request.POST.get('subject', None)
	    		print subject
	    		contact_name = request.POST.get('contact_name', None)
	    		contact_email = request.POST.get('contact_email', None)
	    		content = request.POST.get('content', None)
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
	    			['g_avilez@ikaay.com.mx'],
	    			headers = {'Reply to':contact_email})
	    		email.send()
	    		# return redirect('get')
	    	else:
	    		context['form_errors'] = form.errors
	    		print context['form_errors']
    	return super(HomePage,self).get(request,*args,**kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def contact(request):
	form_class= ContactForm
	return render(request,"contact.html",{'form':form_class},)

class three(generic.TemplateView):
    template_name = "three.html"

class Cascade(generic.TemplateView):
    template_name = "cascade.html"

class ben_frank(generic.TemplateView):
    template_name = "glasses.html"



#view for elasticsearch
# def notes(request):
#     form = PostSearchForm(request.GET)
#     posts = form.search()
#     return render_to_response('notes.html', {'posts': posts})


