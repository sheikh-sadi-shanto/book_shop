from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from e_book.views import book_create

urlpatterns = [
    path('', home,name='home'),
    path('profile_edit',profile_edit,name='profile_edit'),
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('search',search,name='search'),
    path('passchange',passwordchange,name='passchange'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
