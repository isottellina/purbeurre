# views.py --- 
# 
# Filename: views.py
# Author: Louise <louise>
# Created: Mon Apr 27 14:00:21 2020 (+0200)
# Last-Updated: Mon Apr 27 21:31:43 2020 (+0200)
#           By: Louise <louise>
#
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import UserForm

def signup(request):
    """
    Sign-up view.
    """
    if request.method == "GET":
        return render(request, "users/signup.html")
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create(
                username=user_form.cleaned_data['username'],
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data.get('last_name'),
                email=user_form.cleaned_data['email'],
                password=user_form.cleaned_data['password']
            )

            user.save()
            return HttpResponseRedirect(reverse('home:index'))
        else:
            return render(request, "users/signup.html")
