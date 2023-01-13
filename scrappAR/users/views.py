from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationFrom
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("user authenticaed and logged in")
            else:
                return HttpResponse('Invalid credentials')
    else: 
        form = LoginForm()
    return render(request, 'users/login.html',{'form':form})

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