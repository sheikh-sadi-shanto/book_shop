from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('ebook', ebook),
    path('profile',book_create,name='profile'),
    path('edit_book/<int:id>',edit_book,name='edit_book'),
    path('delete_book<int:id>',delete_book,name='delete_book'),
    path('delete_chapter<int:id>',delete_chapter,name='delete_chapter'),
    path('back<int:id>',back,name='back'),
    path('bookpdf<int:id>',bookpdf,name='bookpdf'),
    path('edit_chapter<int:id>',edit_chapter,name='edit_chapter'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
