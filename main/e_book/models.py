from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.dispatch import receiver
from django.db.models.signals import post_save
from all_user.models import User,Profile
# Create your models here.
class Ebook(models.Model):
    user_book=models.ForeignKey(User,on_delete=models.CASCADE)
    
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0.00,null=True,blank=True)
    offer=models.IntegerField(default=0,null=True,blank=True)
    offer_detail=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    book_img=models.ImageField(upload_to='book_img',default='default.jpg')
    def __str__(self) :
        return 'book name : ' +str(self.name)
    def offer_price(self):
        offer_price=self.price - (self.price*(self.offer/100))
        return offer_price

class Book_chapter(models.Model):
    chapter_book=models.ForeignKey(Ebook,on_delete=models.CASCADE,related_name='book_chapter')
    chapter_name=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self) :
        return str(self.chapter_book.name)+'-' +str(self.chapter_name)

class Book_details(models.Model):
    page_detail=models.OneToOneField(Book_chapter,on_delete=models.CASCADE,related_name='detail')
    content=RichTextUploadingField(null=True,blank=True,default='welcome')
    def __str__(self) :
        return str(self.content)




@receiver(post_save, sender=Book_chapter)
def create_book(sender, instance, created, **kwargs):
    if created:
        Book_details.objects.create(page_detail=instance)

@receiver(post_save,sender= Book_chapter)
def save_book(sender, instance, **kwargs):
    instance.detail.save()



