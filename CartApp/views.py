from django.shortcuts import render,redirect
from ShoppingApp.models import product
from .models import Cart,CartItem
from  django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def Cart_id(request):
    Cart=request.session.session_key
    if not Cart:
        Cart=request.session.create()
    return Cart

def add_Cart(request,product_id):
    products=product.objects.get(id=product_id)

    try:
        Cart=add_Cart.objects.get(Cart_id=Cart_id(request))

    except Cart.DoesNotExsits:
        Cart=Cart.objects.create(Cart_id=Cart_id(request))

        Cart.Save(),

    try:
       CartItem=Cart.objects.get(product=product,Cart=Cart)
       if CartItem.quantity < CartItem.product.stock:
         CartItem.quantity+=1
       CartItem.save()

    except CartItem.DoesNotExist:
        CartItem=CartItem.objects.create(product=product,quantity=1,Cart=Cart)
        CartItem.save()
    return redirect('Cart:Cart_detail')

def Cart_detail(request,total=0,counter=0,CartItem=None):
    try:
        Cart=Cart_detail.objects.get(Cart_id=Cart_id(request))
        CartItem=CartItem.objects,filter(Cart=Cart,active=True)

        for CartItem in CartItem:
            total+=(CartItem.product.price*CartItem.quantity)
            counter+=CartItem.quantity
    except ObjectDoesNotExist:
        pass

    return render(request,'Cart.html',dict(CartItem=CartItem,total=total,counter=counter))


def Cart_remove(request,product_id):
    Cart=Cart.objects.get(Cart_id=Cart_id(request))
    product=get.object_or_404(product_id=product_id)
    CartItem=CartItem.objects.get(product=product,Cart=Cart)
    if CartItem.quantity >1 :
        CartItem.quantity -=1
        CartItem.save()
    else:
        CartItem.delete()
    return redirect('Cart:Cart_detail')

def full_remove(request,product_id):
    Cart=Cart.objects.get(Cart_id=Cart_id(request))
    product=get.object_or_404(product_id=product_id)
    CartItem=CartItem.objects.get(product=product,Cart=Cart)
    CartItem.delete()
    return redirect('Cart:Cart_detail')
