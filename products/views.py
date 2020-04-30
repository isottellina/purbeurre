# views.py ---
#
# Filename: views.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:58:05 2020 (+0200)
# Last-Updated: Fri May  1 00:40:25 2020 (+0200)
#           By: Louise <louise>
#
"""
Views for the products app.
"""
from django.shortcuts import render, get_object_or_404
from .models import Product

def search(request):
    """
    Search for a product. Return a search page if there
    is no query. Accepts only GET method and returns the
    same search page if there is a POST request.
    """
    if (request.method != "GET"
        or "query" not in request.GET
        or not request.GET["query"]):
        return render(request, "products/search.html")

    results = Product.objects.filter(name__icontains=request.GET['query'])

    return render(request, "products/search_results.html", {
        'search_str': request.GET['query'],
        'results': results
    })

def substitute(request, product_id):
    """
    Return all substitutes for a product, similar to
    the search function. Returns a 404 error if the
    product doesn't exist.
    """
    product = get_object_or_404(Product, id=product_id)
    substitutes = product.category.products.order_by('nutriscore')[:24]

    return render(request, "products/substitute.html", {
        'orig_product': product,
        'substitutes': substitutes
    })

def info(request, product_id):
    """
    Returns all info on a product.
    """
    product = get_object_or_404(Product, id=product_id)

    return render(request, "products/info.html", {
        'product': product
    })
