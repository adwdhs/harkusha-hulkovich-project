from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile



class Login(View):
    def get(self, request):
        context = {


        }
        return render(request, "login.html", context)
    
    def post (delf, request):

        if request.method == "POST":

            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('home') 
            else: 
                context = {
                    "message": "Account with such credentials doesn't exists"
                }
                return render(request, "login.html", context)
        
        return redirect("login")

class Register(View):
    def get(self, request):
        context = {

        }
        return render(request, "register.html", context)
    
    def post (delf, request):

        if request.method == "POST":

            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            account_type = request.POST.get("account_type")
            context = {}
            if User.objects.filter(username=username).exists():
                # Username already taken
                return render(request, 'register.html', {'err_msg': 'Username already exists'})
            if password1 != password2:
                context["username"] = username
                context["err_msg"] = "Passwords don't matches"
                return render(request, "register.html", context)
                
            else: 
                if account_type == "admin":
                    superuser = User.objects.create_superuser(
                        username=username,                      
                        password=password2
                    )
                    Profile.objects.create(user=superuser)
                    return redirect("login")
                    
                elif account_type == "user":
                    user = User.objects.create_user(
                        username=username,                      
                        password=password2
                    )
                    Profile.objects.create(user=user)
                    return redirect("login")
        
        return redirect("login")    


def logout_view(request):
    logout(request)
    return redirect('home') 