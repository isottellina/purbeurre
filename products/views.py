# views.py --- 
# 
# Filename: views.py
# Author: Louise <louise>
# Created: Sun Apr 26 19:58:05 2020 (+0200)
# Last-Updated: Thu Apr 30 22:10:05 2020 (+0200)
#           By: Louise <louise>
#
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, SavedProduct

def search(request):
    """
    Search for a product. Return a search page if there
    is no query. Accepts only GET method and returns the
    same search page if there is a POST request.
    """
    if (request.method != "GET" or
        "query" not in request.GET or
        not request.GET["query"]):
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

def save(request):
    """
    Saves a substitute. Is intended to be called by
    AJAX calls, and only by POST requests.
    """
    if request.method != "POST":
        # In this case, redirect the user to the front page
        return redirect('home:index')
        
    if not request.user.is_authenticated:
        # In this case, return a error message and an error
        # code
        return JsonResponse(
            {
                "error": "You can only save when you are connected."
            },
            status=401
        )

    if (("orig_product" not in request.POST)
        or ("sub_product" not in request.POST)):
        # When we don't have the info we need, the request is
        # malformed, so error 400.
        return JsonResponse(
            {
                "error": "Your request is malformed."
            },
            status=400
        )

    try:
        orig_product = get_object_or_404(Product,
                                         id=request.POST['orig_product']
        )
        sub_product = get_object_or_404(Product,
                                        id=request.POST['sub_product']
        )
    except Http404:
        # If we couldn't get any of the products, error 404
        return JsonResponse(
            {
                "error": "One of the products indicated doesn't exist."
            },
            status=404
        )

    # If we got through all these hoops, the data we have is good, and
    # we can just save it.
    saved_product = SavedProduct(
        original_product=orig_product,
        replaced_product=sub_product,
        user=request.user
    )
    saved_product.save()

    # Finally we can return a 200 code.
    return JsonResponse(
        {
            "error": "The product was successfully saved."
        }
    )
