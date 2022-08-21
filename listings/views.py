from django.shortcuts import render
from random import choice
from .models import Listing
from main.views import check_auth
from main.models import Account
from .filters import ProductFilter
# Create your views here.

def listing_page(request,listing_id):
    listing=Listing.objects.get(id=listing_id)
    print(request)
    print(listing)
    return render(request,'listings/listing_page.html', {'listing':listing})

def listing_catalog(request): #For catalog
    check_auth(request)
    acc = Account.objects.get(user=request.user)
    listings=Listing.objects.filter(account=acc)
    f = ProductFilter(request.GET, queryset=listings)

    if request.method == "POST":
        print('hello')
        print(request.POST)

    return render(request,'listings/listing_catalog.html',{'listings':f.qs,'filter':f})

def listing_preuploaded(request): #For catalog
    check_auth(request)
    acc = Account.objects.get(user=request.user)
    listings=Listing.objects.filter(account=acc,is_etsy=False)


    return render(request,'listings/pre_uploaded.html',{'listings':listings})

def shop_page(request): #General page of our shop
    return render(request,'main/layout.html')

def competitor(request): #For competitors page
    return render(request,'main/layout.html')