from django.urls import path
from .import views
app_name='Cart'

urlpatterns=[
    path('add/<int:product-id/',views.add_Cart,name='add_Cart'),
    path('',views.Cart_detail,name='Cart_detail'),
    path('remove/<int:product_id>/',views.Cart_remove,name='Cart-remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
]