from django.contrib.auth import authenticate, logout, login

def login_service(user ,request):
    login(request, user)

def authentication_login(username, password, request):
    user = authenticate(username=username, password=password)
    if not user:
        return False
    else:
        if user.is_active:
            login_service(request, user)
            return True
        else:
            return False

def authentication_logout(request):
    logout(request)

def exists_username(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False

def create_userProfile(data):
    u = User.objects.create_user(data.username,data.email,data.password)
    u.fist = data.first
    u.last = data.last
    u.save()
    up = UserProfile()
    up. 

