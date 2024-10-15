from django.shortcuts import render
from ShoppingApp.models import product
from django.db.models import Q


# Create your views here.

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products=product.objects.all(),filter(Q (name__contains=query) , Q(description_contain))
    return render(request,'search.html',{'query':query,'products':products})

