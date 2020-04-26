# views.py --- 
# 
# Filename: views.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:58:05 2020 (+0200)
# Last-Updated: Sun Apr 26 19:59:53 2020 (+0200)
#           By: Louise <louise>
# 
from django.shortcuts import render

def index(request):
    return render(request, "products/index.html")
