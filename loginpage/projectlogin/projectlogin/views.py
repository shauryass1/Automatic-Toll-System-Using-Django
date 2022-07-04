from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    return render(request, 'register.html')


def index(response):
    return render(response, 'home.html')


def handlelogin(request):
    emailogin= request.POST['exampleInputEmail1']
    passs = request.POST['exampleInputPassword1']

    user = authenticate(request, username=emailogin, password=passs)

    if user is not None:
        login(request, user)
        return render(request, 'LoginHome.html')

    else:
        messages.error(request, 'incorrect password')
        return redirect('/')


def mapage(request):
    return render(request, 'mapage.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def paybill(request):
    return render(request, 'paybill.html')


def loginhome(request):
    dic = request.user.last_name
    return render(request, 'LoginHome.html', dic)


def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'your account has been successfully created')
        return render(request, 'home.html')

    else:
        return render(request, 'registration.html')


