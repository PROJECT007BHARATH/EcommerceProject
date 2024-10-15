from .models import Cart,CartItem
from .views import Cart_id

def counter(request):
    item_count=0
    if  'admin' in request.path:
        return {}
    else:
        try:
            Cart=Cart_id.objects,filter(Cart_id=Cart_id(request))
            Cart_Item=Cart.objects.all(),filter(Cart=Cart[:1])
            for CartItem in Cart_Item:
                item_count+=Cart_Item.quantity

        except Cart.DoesNotExist:
            item_count=0

    return dict (item_count=item_count)