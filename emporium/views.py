from django.shortcuts import render

def product_listing(request):
    return render(request, 'emporium/product_listing.html', {})
