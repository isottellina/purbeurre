# views.py --- 
# 
# Filename: views.py
# Author: Louise <louise>
# Created: Sun Apr 26 21:16:55 2020 (+0200)
# Last-Updated: Mon Apr 27 23:22:00 2020 (+0200)
#           By: Louise <louise>
# 
from django.shortcuts import render

def index(request):
    """
    Home page of the site.
    """
    return render(request, 'home/index.html')

def legal(request):
    """
    Legal notices.
    """
    return render(request, 'home/legal.html')
