from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from e_book.models import Ebook
from django.contrib.auth.decorators import login_required
from .form import Address
from .models import *
from django.http import HttpResponse
from e_book.models import Ebook
# Create your views here.
def detail_page(request,id):
    product=Ebook.objects.get(id=id)
    return render(request,'productdetail.html',{'product':product})

@login_required(login_url='signin')
def addtorcard(request,id):
    item = get_object_or_404(Ebook, id=id)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print("If Order exist")
        print(order)
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated.")
            return redirect("/")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart.")
            return redirect("/")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to your cart.")
        return redirect("/")



@login_required(login_url='signin')
def cartview(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)

    orders = Order.objects.filter(user=request.user, ordered=False)
    total=float (0)
    for i in carts:
        total=total+float(i.get_total())
    charge=70
    totals=total+charge
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'addtocart.html', context={'carts':carts,'charge':charge,'total':total,'totals':totals, 'order':order})
    else:
        messages.warning(request, "You don't have any item in your cart!")
        # return redirect("/")
    return render(request,'addtocart.html')


# @login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Ebook, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed form your cart")
            return redirect("cartview")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("/")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("/")
    

def cart_del(request):
    cart=Cart.objects.filter(user=request.user)
    cart.delete()
    return redirect('cartview')



# @login_required
def increase_cart(request, id):
    item = get_object_or_404(Ebook, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been inreased")
                return redirect("cartview")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("/")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("/")


# @login_required
def decrease_cart(request, id):
    item = get_object_or_404(Ebook, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been decreased")
                return redirect("cartview")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} item has been removed from your cart")
                return redirect("cartview")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("/")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("/")


def checkout(request):
    cart = Cart.objects.filter(user=request.user, purchased=False)
    # instanc=get_object_or_404(User,)
    form=Address()
    if request.method=='POST':
        form=Address(request.POST)
        if form.is_valid():
            form.save()
    total=float (0)
    for i in cart:
        total=total+float(i.get_total())
    charge=70
    totals=total+charge
    print(totals)
    return render(request,'checkout.html',{'form':form,'item':cart,'totals':totals,'total':total,'charge':charge,})

