from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.http import HttpResponse
from  django.contrib.auth.decorators import login_required
from . models import blog,index


# Create your views here.

def home(request):
    return render(request,'first_app/index.html')
def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['psw'])
        if user is not None:
            auth.login(request,user)

            return redirect('home')
        else:
            return render(request,'first_app/login.html',{'error':'oops! username or password does not match'})
    else:
         return render(request,'first_app/login.html')
def logout(request):
    if request.method=='POST':

        auth.logout(request)
        return redirect('login')
        return render(request,'first_app/login.html',{'y':'loged out'})

def signup(request):
    if request.method=='POST':
        if request.POST['psw1'] == request.POST['psw2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'first_app/signup.html',{'error':'username already taken'} )
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['psw1'],email=request.POST['email'])
                auth.login(request,user)
                return render(request,'first_app/signup.html',{'hey':'username created and you have loged in sucessfully  '} )
                return redirect('home')

        else:
            return render(request,'first_app/signup.html',{'hey1':'password does not match'} )
    else:
        return render(request,'first_app/signup.html')
@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            Blog=blog()
            Blog.title=request.POST['title']
            Blog.body=request.POST['body']
            Blog.image=request.FILES['image']
            Blog.pub_date=timezone.datetime.now()
            Blog.hunter=request.user
            Blog.save()
            return redirect('/home/blog/'+str(Blog.id))
        else:
            return render(request,'first_app/create.html',{'error':'plz fill all entries'})
    else:
        return render(request,'first_app/create.html')
def detail(request,Blog_id):
    Blog= get_object_or_404(blog,pk=Blog_id)
    return render(request ,'first_app/detail.html',{'blogs':Blog})
def allb(request):

    posts = blog.objects
    return render(request, 'first_app/allblog.html', {'blogs': posts})
# def about(request):
#     return render(request,'first_app/about.html')
def detailf(request):
    return redirect('/home/blog/'+str(Blog.id))



def detail1(request,Index_id):
    Blog= get_object_or_404(index,pk=Index_id)
    return render(request ,'first_app/indexdetail.html',{'blogs1':Blog})
def allb1(request):
    posts = index.objects
    return render(request, 'first_app/index.html', {'blogs1': posts})
def detailf1(request):
        return redirect('/home/index/'+str(Index.id))
