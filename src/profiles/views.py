from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.contrib.auth.mixins import AccessMixin
from . import forms
from . import models
from django.http import HttpResponse
 
from django.utils import timezone
from django.shortcuts import render
from .models import Post, Video
from .forms import ShopFor, PostForm
import shop.models  
from shop.models import Product
from django.contrib.auth.decorators import login_required
from authtools.models import User 
from django.views.generic import ListView, DetailView
from .models import Video
  
class ShowProfile(AccessMixin,TemplateView):
    template_name = "profiles/show_profile.html"  
    http_method_names = ['get', 'post' ]
    def get(self, request, *args, **kwargs):
        # name=self.kwargs.get('name')
        # u = get_object_or_404(User,name=name)
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            #add anonymoues user?
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        # print products by profile kwargs returns a dictionary
        products = Product.objects.filter(author=user).order_by('?')
        videos = Video.objects.filter(author=user)
        kwargs['products']= products
        kwargs['videos']=videos
        return super(ShowProfile, self).get(request, *args, **kwargs)
    

    # show us all products in ShowProfile
    # def get_context_data(self,**kwargs):
    #     context = super(ShowProfile, self).get_context_data(**kwargs)
    #     context['products'] =Product.objects.filter(available=True)
    #     return  context

class UserProfileView(DetailView):
    model = User
    slug_field = "name"
    template_name = "profiles/show_profile.html"

class EditProfile(LoginRequiredMixin,TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "saved details")
        return redirect("profiles:show_self")




#Add new product for sell
def post_new(request):
        if request.method == "POST":
            form = ShopFor(request.POST,
                         request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect("profiles:show_self")
        else:
            form = ShopFor()
        return render(request, 'profiles/product_add.html', {'form': form})



# def post_new(request):
#         if request.method == "POST":
#             form = PostForm(request.POST)
#             if form.is_valid():
                
#                 post = form.save(commit=False)
#                 post.author = request.user
#                 post.published_date = timezone.now()
#                 post.save()
#                 return redirect('/')
#         else:
#             form = PostForm()
#         return render(request, 'profiles/product_add.html', {'form': form})


class PostVideo(ListView):
    model = Video


