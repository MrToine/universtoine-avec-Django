from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from .models import Profile

def loginUser(request):
    message_error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
    
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('news:index'))
            if not user.is_active:
                print("user non actif")
                message_error = "Ton compte n'est pas activé. Vérifie bien tes email et active le."
        else:
            message_error = "Utilisateur introuvable. Si tu es inscrit, ton compte n'est peut-être pas activé. Vérifie bien tes email et active le."
    
    return render(request, 'users/login.html', {'message_error': message_error})

def logoutUser(request):
    message_error = ""
    logout(request)
    return HttpResponseRedirect(reverse('news:index'))

def registerUser(request):
    errors = 0
    message_error = ()
    message_success = ""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        
        if username and email and password and repeat_password:
            if password != repeat_password:
                errors += 1
                message_error = message_error + ("Les mots de passe ne correspondent pas",)
            
            if User.objects.filter(username=username).exists():
                errors += 1
                message_error = message_error +  ("Pseudo déjà existant",)

            if User.objects.filter(email=email).exists():
                errors += 1
                message_error = message_error +  ("Email déjà existant",)
        else:
            errors += 1
            message_error = message_error + ("Tout les champs doivent être renseignés",)
        
        if errors <= 0:
            user = User.objects.create_user(username, email, password)
            profile_user = Profile(user=user)
            profile_user.save()
            user.save()
            message_success = "Bienvenue sur le site " + user.username + " tu es désormais inscris !"
        
    return render(request, 'users/register.html', {"errors": errors,"message_error": message_error, 'message_success': message_success})