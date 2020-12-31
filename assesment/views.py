from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import logout


# Create your views here.
from assesment.forms import UserCreate


class DashboardView(TemplateView):
    template_name = 'assesment/dashboard.html'


class Signup(CreateView):
    # Creating a new user.
    template_name = "assesment/signup.html"
    form_class = UserCreate
    model = User
    success_url = '/assesment/dashboard/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(self.request, user)
            return redirect(reverse("assesment:signup"))
        return render(self.request, self.template_name)


class CustomLogout(TemplateView):
    template_name = "assesment/logout.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        logout(request)
        response.delete_cookie("email")
        response.delete_cookie("first_name")
        response.delete_cookie("last_name")
        response.delete_cookie("username")
        return response

