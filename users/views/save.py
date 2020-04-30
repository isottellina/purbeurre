# views_save.py --- 
# 
# Filename: views_save.py
# Author: Louise <louise>
# Created: Thu Apr 30 23:06:31 2020 (+0200)
# Last-Updated: Thu Apr 30 23:16:10 2020 (+0200)
#           By: Louise <louise>
# 
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import SavedProduct
from products.models import Product

def save(request):
    """
    Saves a substitute. Is intended to be called by
    AJAX calls, and only by POST requests.
    """
    # We scope these imports in the function
    from products.models import Product
    
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
        orig_product=orig_product,
        sub_product=sub_product,
        user=request.user
    )
    saved_product.save()

    # Finally we can return a 200 code.
    return JsonResponse(
        {
            "error": "The product was successfully saved."
        }
    )

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
