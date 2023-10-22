from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('detail_page<int:id>', detail_page,name='detail_page'),
    path('cart<int:id>', addtorcard,name='cart'),
    path('remove_from_cart<int:id>', remove_from_cart,name='remove_from_cart'),
    path('increase_cart<int:id>', increase_cart,name='increase_cart'),
    path('decrease_cart<int:id>', decrease_cart,name='decrease_cart'),
    path('cartview', cartview,name='cartview'),
    path('checkout', checkout ,name='checkout'),
    path('cart_del', cart_del ,name='cart_del'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
