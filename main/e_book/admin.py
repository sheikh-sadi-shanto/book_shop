from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Ebook)
class Mybook(admin.ModelAdmin):
    list_display = ('id','name','price','book_img')

@admin.register(Book_chapter)
class Mychapter(admin.ModelAdmin):
    list_display = ('id','chapter_name')

@admin.register(Book_details)
class Mychapter(admin.ModelAdmin):
    list_display = ('id',)
