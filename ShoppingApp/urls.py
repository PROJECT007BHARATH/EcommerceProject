from django.urls import path
from .import views
app_name='shop'

urlpatterns = [
        path('',views.allprodcat,name='allprodcat'),
        path('<slug:C_slug>/',views.allprodcat,name='product_by_category'),
        path('<slug:C_slug>/<slug:product_slug>/',views.ProDetail,name='ProdCatdetail'),

]
