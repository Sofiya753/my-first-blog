from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')
def ad(request):
    return render(request, 'ad/ad.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        form= CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Аккаунт для '+user+ ' создан!')
                return redirect('login')
        context={ 'form': form}
        return render(request,'mainApp/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is  not None :
                login(request,user)
                return redirect('homePage')
            else:
                messages.info(request, 'Пароль или логин введены некорректно!')
        contex={}
        return render(request,'mainApp/login.html',contex)

def logoutUser(request):
    logout(request)
    return redirect('homePage')
