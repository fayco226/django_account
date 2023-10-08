from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import json

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Mot de passe ou Nom d'utilisateur incorect"
        else:
            resp['msg'] = "Mot de passe ou Nom d'utilisateur incorect"
    return HttpResponse(json.dumps(resp),content_type='application/json')
