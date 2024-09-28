from django.contrib.auth.models import User as AUser, Group
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
from rest_framework.authtoken.models import Token


def create_drf_token(auser):
    try:
        Token.objects.create(user=auser)
    except Exception:
        pass


def login_user(request, handle):
    auser = authenticate(username=handle, password=handle)
    if auser is not None:
        create_drf_token(auser)
        login(request, auser)
        return True
    else:
        return False


def logout_user(request):
    logout(request)


def is_user_logged(request):
    return request.user.is_authenticated


def get_auser(handle):
    return AUser.objects.get(email=handle)


def get_csrf_token(request):
    token = csrf.get_token(request)
    if token is None:
        token = 'NOTPROVIDED'
    return token


def get_drf_token(auser):
    return Token.objects.get(user=auser)


def has_permission(user, permission, model_name):
    permission_str = "main_system." + permission + "_" + model_name
    auser = get_auser(user.email)
    return auser.has_perm(permission_str)