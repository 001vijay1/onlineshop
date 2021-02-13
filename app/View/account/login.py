from django.shortcuts import render,redirect
from django.contrib.auth import login as django_login,logout as django_logout,authenticate
from app.form.login_form import LoginForm
from django.contrib import messages

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                django_login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Access denied!')
        else:
            messages.error(request,'Access denied!')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})

def logout(request):
    django_logout(request)
    return redirect('home')