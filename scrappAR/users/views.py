from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import signupForm, loginForm
from django.http import HttpResponse
from django.views import View
from django.contrib import messages, auth
# Create your views here.
def loginPage(request):
    form = loginForm(request.POST)

    if request.method == 'POST':
        if request.POST.get('UserName') is None or request.POST.get('Password') is None:
            messages.error(request, 'Please enter your username or password.')
            return render(request, 'users/signup.html')
        else:
            user = auth.authenticate(username = request.POST.get('UserName'), password = request.POST.get('Password'))

            if user is not None:
                auth.login(request, user)
                return redirect('discover:discover')
            else:
                messages.success(request, 'You have successfully login.')
                return redirect('discover:discover')
            # render(request, 'users/index.html')
    else:
        return render(request, 'users/login.html')

def signout(request):
    
    auth.logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('login')

def signupPage(request):
    #form = signupForm(request.POST)
    #if form.is_valid():
    context = {}
    if request.method == "POST":
        while request.POST.get('txtPassword2') == request.POST.get('txtPassword'):
                try:
                    User.objects.get(username = request.POST.get('txtUserName'))
                    
                    return render (request,'users/signup.html', {'error':'Username is already taken!'})
                except User.DoesNotExist:
                    newuser = User.objects.create_user(username = request.POST.get('txtUserName'), first_name = request.POST.get('txtFirstName'),last_name = request.POST.get('txtLastName'), email = request.POST.get('txtEmail'), password = request.POST.get('txtPassword'))
                    
                    auth.login(request, newuser)
                    return redirect('discover:discover')
        else:
            messages.error(request, 'Password does not match!')
            return render(request, 'users/signup.html', context)
    else:
        return render(request, "users/signup.html",context)

def resetPage(request):
    return render(request, 'users/resetpassword.html')