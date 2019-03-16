from django.views import View
from django import forms
from .models import UserAccount
from customer.forms import RegistrationForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

User = get_user_model()  #a


class RegistrationView(View):
    template = 'auth/registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):  # Something from stack_over_flow
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)  # new instance
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user.set_password(password)
            password_check = form.cleaned_data['password_check']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            new_user.save()
            UserAccount.objects.create(user=User.objects.get(username=new_user.username),
                                       first_name=new_user.first_name,
                                       last_name=new_user.last_name,
                                       email=new_user.email)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(self.request, self.template, context)
