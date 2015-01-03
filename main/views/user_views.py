from django.shortcuts import render, redirect
from main.services import user_services
from django.contrib.auth.decorators import login_required

def index_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('main:dashboard')
        else:
            return redirect('main:login')

def login_view(request):
    if request.method == 'POST':
        usrname = request.POST['username']
        password = request.POST['password']
        if user_services.authentication_login(usrname,password,request):
            return redirect('main:dashboard')
        else:
            return render(request,'main/user_views/login_view',{'error':True})
    else:
        return render(request,'main/user_views/login_view.html',{})

@login_required
def logout_view(request):
    user_services.authentication_logout(request)
    return redirect('main:index')

@login_required
def home_page_view(request):
    return render(request,'main/user_views/home_page_view.html',{})

def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        if user_services.exists_username(username):
            return render(request,'main/user_views/registration_view.html',{'errUsr':True})
        if request.POST['pass1'] != request.POST['pass2']:
            return render(request,'main/user_views/registration_view.html',{'errPass':True})
        user = user_services.new_user_profile(username,password,email,name,last)
        user_services.login_service(user,request)
        return redirect('main:index')
    else:
        return render(request,'main/user_views/registration_view.html',{})

@login_required
def editor_view(request):
    pass
