# views.py --- 
# 
# Filename: views.py
# Author: Louise <louise>
# Created: Sun Apr 26 21:16:55 2020 (+0200)
# Last-Updated: Sun Apr 26 21:17:03 2020 (+0200)
#           By: Louise <louise>
# 
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
