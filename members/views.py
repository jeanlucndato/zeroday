from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404 
from django.views import generic
from django.views.generic import DetailView 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout 
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from zeroday.models import Profile


# Create your views here.

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile', 'website_url', 'facebook_url', 'twitter_url', 'linkdin_url', 'github_url', 'blogger_url']
    success_url = reverse_lazy('home')
    


class ShowProfilePageView(DetailView):
    model = Profile 
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context["page_user"] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
  
    
def password_success(request):
    return render(request, 'registration/passord_success.html', {})
    
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
def logout_view(request):
    # Déconnectez l'utilisateur
    logout(request)
    # Redirigez vers la page d'accueil ou une autre page de votre choix
    return redirect('home')

