from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def loginUser(request):
    message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
    
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('news:index'))
        else:
            message = "Utilisateur introuvable"
    
    return render(request, 'users/login.html', {'message': message})

def logoutUser(request):
    message = ""
    logout(request)
    return HttpResponseRedirect(reverse('news:index'))

def registerUser(request):
    message = ""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        
        user = authenticate(username=username, email=email)
        if user is not None:
            message = "Pseudo ou email déjà existant"
        else:
            message = "Aucun utilisateur trouvé, inscription possible"
        
    return render(request, 'users/register.html', {"message": message})