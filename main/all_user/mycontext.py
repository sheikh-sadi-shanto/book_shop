
from .models import Profile
from buy_app.models import Cart

def ok(request):
    try:
        cart_item=Cart.objects.filter(user=request.user)
        user_profile1=Profile.objects.get(user=request.user)
        return {'user_profile1':user_profile1,'cart_item':cart_item}
    except:
        user_profile1=None
    
    return {'user_profile1':user_profile1}