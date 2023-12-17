from django.db import models
from all_user.models import User
from e_book.models import Ebook
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
    item=models.ForeignKey(Ebook,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    purchased=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user} X {self.quantity} X {self.item}'

    def get_total(self):
        if self.item.offer:
            total = float(self.item.offer_price()) * self.quantity
        else:
            total=float(self.item.price) * self.quantity
        float_total = format(total, '0.2f')
        return float_total
    
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return str(self.user)+'-'+str(self.ordered)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total

class BillingAdress(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=120)
    number=models.IntegerField()
    distric=models.CharField(max_length=120)
    address=models.TextField()
    

