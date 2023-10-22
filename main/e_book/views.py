from django.shortcuts import render,redirect,get_object_or_404,reverse
from all_user.models import User,Profile
from django.contrib.auth.decorators import login_required
from .models import Ebook,Book_chapter,Book_details
from django.db.models import Q
from .form import YourForm
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.
def ebook(request):
    book_list=Ebook.objects.filter(user_book=request.user)
    return render(request,'book.html',{'book_list':book_list})

@login_required(login_url='signin')
def book_create(request):
    profile_detail=Profile.objects.get(user=request.user)
    book_user=Ebook.objects.filter(user_book=request.user)
    # print(book_user)
    if request.method=='POST':
        cbook=request.POST.get('name')
        user=Ebook.objects.create(user_book=request.user,name=cbook)
        user.save()
    return render(request,'profile.html',{'all_book':book_user,'profile_detail':profile_detail})

def edit_book(request,id):
    specific=Ebook.objects.get(user_book=request.user,id=id)
    chap=Book_chapter.objects.filter(chapter_book=specific)
    if request.method=='POST':
        chapter_instance=request.POST.get('chapte')
        if chapter_instance!=None and chapter_instance!='':
            chapter=Book_chapter.objects.create(chapter_book=specific,chapter_name=chapter_instance)
            chapter.save()

    if request.method=='POST':
        cover_img=request.FILES.get('book_img')
        name=request.POST.get('name')
        off=request.POST.get('offer')
        des=request.POST.get('description')
        offerdescription=request.POST.get('offerdescription')
        price=request.POST.get('price')

        print(off)
        if cover_img!= None and cover_img!='':
            specific.book_img=cover_img
            specific.offer=off
            specific.description=des
            specific.name=name
            specific.price=price
            specific.offer_detail=offerdescription
            specific.save()
        if cover_img== None or cover_img=='':
            specific.name=name
            specific.price=price
            specific.offer=off
            specific.description=des
            specific.offer_detail=offerdescription
            specific.save()
    return render(request,'edit_book.html',{'specific':specific,'chap':chap})




def bookpdf(request,id):
    # print(id)
    book=Ebook.objects.get(id=id)
    all_chapter=Book_chapter.objects.filter(chapter_book=book)
    # print(all_chapter)
    # pages=Book_details.objects.filter(page_detail=all_chapter)
    # print(pages)
    for i in all_chapter:
        # print(i)
        ca=Book_chapter.objects.get(id=i.id)
        # print(ca)
        details=Book_details.objects.filter(page_detail=ca)

    tem=get_template('book.html')

    context={'book':book,'all_chapter':all_chapter}
    html=tem.render(context)
    respon=HttpResponse(content_type='application/pdf')
    respon['Content-Disposition']='filename"yourfile.docx"'

    pisa_status=pisa.CreatePDF(html,dest=respon)
    if pisa_status.err:
        return HttpResponse('problem '+html+'ok')
    
    return respon



def edit_chapter(request,id):

    cha=Book_chapter.objects.get(id=id)
    details=Book_details.objects.filter(page_detail=cha)
    if request.method=='POST':
        a=request.POST.get('ch')
        if a!=None and a!='':
            cha.chapter_name=a
            cha.save()
            # previous_page = reverse('edit_book',args=[bookid])
            # return redirect(previous_page)
    try:
        form=YourForm(instance=details[0])
    except:
        form=YourForm()
    if request.method=='POST':
        form=YourForm(instance=details[0],data=request.POST)
        if form.is_valid():
            form.save()
            form=YourForm(instance=details[0],data=request.POST)
    return render(request,'edit_chapter.html',{'cha':cha,'details':details,'form':form})



def delete_book(request,id):
    dell=get_object_or_404(Ebook,id=id)
    print(dell.name)
    dell.delete()
    return redirect('profile')

def delete_chapter(request,id):
    chapter=Book_chapter.objects.get(id=id)
    bookid=chapter.chapter_book.id
    del_chapter=get_object_or_404(Book_chapter,id=id)
    print(del_chapter.chapter_name)
    del_chapter.delete()
    previous_page = reverse('edit_book',args=[bookid])
    return redirect(previous_page)

def back(request,id):
    chapter=Book_chapter.objects.get(id=id)
    bookid=chapter.chapter_book.id
    previous_page = reverse('edit_book',args=[bookid])
    return redirect(previous_page)

