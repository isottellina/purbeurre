# forms.py --- 
# 
# Filename: forms.py
# Author: Louise <louise>
# Created: Mon Apr 27 20:55:38 2020 (+0200)
# Last-Updated: Mon Apr 27 20:59:15 2020 (+0200)
#           By: Louise <louise>
# 
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=255)
    first_name = forms.CharField(label="Prénom",
                                 max_length=30)
    last_name = forms.CharField(label="Nom de famille",
                                max_length=30,
                                required=False)
    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(label="Mot de passe")
    
