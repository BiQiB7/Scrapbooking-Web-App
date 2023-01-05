from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# use API for authentication
from django.contrib.auth import logout, views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView

# registration form
from users.forms import RegisterForm

# Models
from users.models import Profile
# to add post model


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save() #save the user details if the form is valid
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
