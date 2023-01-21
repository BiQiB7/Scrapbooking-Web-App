from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, UserRegistrationFrom
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('UserName')
        password = request.POST.get('Password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users/login.html')
        else:
            messages.error(request, 'Username OR password invalid')

    context = {}
    return render(request, 'main/index.html', context)


def user_registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationFrom(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit = False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'users/register_done.html')
    else:
        user_form = UserRegistrationFrom()
    return render(request, 'users/register.html',{'user_form':user_form})