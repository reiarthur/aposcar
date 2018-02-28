from django.contrib.auth.views import LoginView as liv
from django.contrib.auth.views import LogoutView as lov
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    FormView,
    TemplateView
    )
from django.urls import reverse_lazy
from .forms import *

class LoginView(liv):
    template_name = 'accounts/login.html'
    
class LogoutView(lov):
    next_page = reverse_lazy('core:index')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('core:index')
    
    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data['password1'])
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


@login_required
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'
