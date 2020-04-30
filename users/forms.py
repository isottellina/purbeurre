# forms.py ---
#
# Filename: forms.py
# Author: Louise <louise>
# Created: Mon Apr 27 20:55:38 2020 (+0200)
# Last-Updated: Thu Apr 30 23:42:38 2020 (+0200)
#           By: Louise <louise>
#
"""
Just a form to check the data given to the registration page.
"""
from django import forms

class UserForm(forms.Form):
    """
    The form in question. Checks that required labels are
    present and that the e-mail is correct.
    """
    username = forms.CharField(label="Nom d'utilisateur",
                               max_length=255)
    first_name = forms.CharField(label="Prénom",
                                 max_length=30)
    last_name = forms.CharField(label="Nom de famille",
                                max_length=30,
                                required=False)
    email = forms.EmailField(label="Adresse e-mail")
    password = forms.CharField(label="Mot de passe")
