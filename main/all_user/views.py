from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm,Signin_Form,Profile_Form,Passchangeform
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from .models import User,Profile
from e_book.models import Ebook
from buy_app.models import Cart
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    al=User.objects.filter(premium=True)
    all_book=Ebook.objects.filter(user_book__in=al)
    
    return render(request,'index.html',{'all_book':all_book})

def signup(request):
    signup_form=SignupForm()
    if request.method=='POST':
        signup_form=SignupForm(request.POST)
        if signup_form.is_valid():
            messages.success(request, f'Your account has been created! You may now login.')
            signup_form.save()
    return render(request,'signup.html',{'signup_form':signup_form})

def signin(request):
    signin_form=Signin_Form()
    if request.method=='POST':
        signin_form=Signin_Form(request.POST)
        if signin_form.is_valid():
            email = signin_form.cleaned_data.get('email')
            password = signin_form.cleaned_data.get('password') 
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                print('login success')
                a=Profile.objects.get(user=request.user)
                print(a.name,'none')
                if a.name==None or a.name=='':
                    return redirect ('profile_edit')
                else:
                    return redirect ('profile') 
            else:
                messages.error(request,'Invalid email and password, plaese try gaan')
    return render(request,'signin.html',{'signin_form':signin_form})

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def profile_edit(request):
    us=Profile.objects.get(user=request.user)
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['addess']
        img=request.FILES.get('pro_pic')
        if img!=None:
            us.name=name
            us.addess=address
            us.pro_pic=img
            us.save()
        if img==None:
            us.name=name
            us.addess=address
            us.save()
 
    profile_form=Profile_Form({'name':us.name,'addess':us.addess})   
    return render(request,'profile_edit.html',{'profile_form':profile_form,'us':us})

@login_required(login_url='signin')
def passwordchange(request):
    passform=Passchangeform(request.user)
    print(request.user.is_authenticated)
    if request.method =='POST':
        passform=Passchangeform(request.user,request.POST)
        if passform.is_valid():
            messages.success(request,'password change successfully ')
            passform.save()
            print('done')
            return redirect('profile')
    if request.method =='GET':
        print('pass get method')
    return render(request, 'changepassword.html',{'passform':passform})

def search(request):
    a=''
    search=request.POST.get('search')
    a=Ebook.objects.filter(Q (name__icontains=search)|Q (price__icontains=search)|Q(description__icontains=search)).distinct()
    paginator = Paginator(a,1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html',{'page_obj':page_obj})

