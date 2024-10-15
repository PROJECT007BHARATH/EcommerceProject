import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from ShoppingApp.models import product


# Create your views here.

# def index(request):
#   return HttpResponse('hey am here')


def allprodcat(request, C_slug=None):
    C_page = None
    products_list = None

    if C_slug is not None:
        C_page = get_object_or_404(category, slug=C_slug)
        products_list = product.objects.all(), filter(category=C_page, available=True)

    else:
        products_list = product.objects.all(), filter(available=True)
        Paginator = product(products_list, 6)

    try:
        page=int(request.GET.get('page','/'))

    except:
        page=1

    try:
        products=Paginator.page(page)

    except(EmptyPage,InvalidPage):
        products=Paginator.page(Paginator.num_page)

        # products = product.objects.all(), filter(available=True) C_page, 'products': products})
    return render(request, "category.html", {'category': C_page, 'Paginator': Paginator})


def ProDetail(request, C_Slug, product_slug):
    try:
        products = product.objects.get(category__slug=C_Slug, Slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'product.html', {'product': product})
