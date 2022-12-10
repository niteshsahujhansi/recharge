from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required # for function based view
from django.utils.decorators import method_decorator # for class based view
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .models import Combo, Internet, Talktime
from . import models
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

# @login_required    
def home(request):
    username = request.user.username
    return render(request,"accounts/home.html",{'username':username})

def registration(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations!! Registered Successfully")
            form.save()
        return render(request, 'accounts/registration.html', {'form':form})
    
    form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form':form})

def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = auth_login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form, 'title':'log in'})

def combo(request):
    context={
        "combo" : Combo.objects.all(),
    }
    combo = Combo.objects.all()
    return render(request,"accounts/combo.html",context)

def internet(request):
    context={
        'net' : Internet.objects.all(),
    }
    return render(request,"accounts/internet.html",context)

def talk(request):
    context={
        'talk' : Talktime.objects.all(),
    }
    return render(request,"accounts/talk.html",context)

def browse(request):
        id = request.POST.get("pack_id")
        db = request.POST.get("db_name")
        fn = getattr(models, db)
        result =  fn.objects.all().filter(id = id).values()[0]
        context = {
            "result" : result,
            "db" : db
        }        
        return render(request,"accounts/browse.html",context)

@login_required
def checkout(request):
    recipient_list = []
    subject = 'Confirmation'
    message = ' Your mobile recharge has been successfull.'
    email_from = settings.EMAIL_HOST_USER

    recipient_list.append(request.user.email)
    
    send_mail( subject = subject, message = message, from_email= email_from,recipient_list= recipient_list, fail_silently=False)
    context = {
       'msg' : 'Email has been sent'
    }
    return render(request,"accounts/checkout.html",context)