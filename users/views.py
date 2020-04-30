# views.py --- 
# 
# Filename: views.py
# Author: Louise <louise>
# Created: Mon Apr 27 14:00:21 2020 (+0200)
# Last-Updated: Thu Apr 30 22:28:40 2020 (+0200)
#           By: Louise <louise>
#
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
            user_already_exists = User.objects.filter(
                username=user_form.cleaned_data['username']
            ).exists()
            
            if user_already_exists:
                # If the user already exists, fail with a
                # HTTP 409 Conflict code.
                return render(request,
                              "users/signup.html",
                              status=409)
            
            user = User.objects.create_user(
                username=user_form.cleaned_data['username'],
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data.get('last_name'),
                email=user_form.cleaned_data['email'],
                password=user_form.cleaned_data['password']
            )

            user.save()
            login(request, user)
            return redirect('home:index')
        else:
            # Return a HTTP 400 Bad Request code
            return render(request, "users/signup.html", status=400)

def signin(request):
    if request.method == "GET":
        return render(request, "users/signin.html")
    elif request.method == "POST":
        # Since we only have to test if the fields are present
        # we don't need a Form.
        try:
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user is not None:
                login(request, user)
                if "next" in request.POST:
                    return redirect(request.POST['next'])
                else:
                    return redirect('home:index')
            error_message = "Nom d'utilisateur ou mot de passe incorrect"
        except KeyError: # a field was missing
            error_message = "Un des deux champs était vide"
        return render(request,
                      "users/signin.html",
                      {
                          "error_message": error_message
                      },
                      status=400
        )
        
def signout(request):
    logout(request)
    return redirect('home:index')

@login_required
def account(request):
    return render(request, "users/account.html")

@login_required
def show_saved(request):
    """
    Show the saved products of a user.
    """
    savedproducts = request.user.saved_products.all()
    products = [savedproduct.replaced_product
                for savedproduct in savedproducts]
    
    return render(request, "users/show_saved.html", {
        "products": products
    })
