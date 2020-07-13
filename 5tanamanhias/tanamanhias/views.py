from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def index(request):
     context = {
          'title':'Orplant',

     }

     print(request.user.is_authenticated())
     template_name = None
     if request.user.is_authenticated():
         template_name = 'index_user.html'
     else:
         template_name = 'index.html'    
     return render(request, template_name, context)


def loginView(request):
    context = {
              'title':'Orplant',
              'deskripsi':'halaman login'

     }

    user = None
    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('index')
        else:
            return render(request, 'login.html', context)

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        print(username_login)
        user = authenticate(request, username = username_login, password = password_login)
        print(user, 'ini user nya ')
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')
            
    print("masuk")
    return render(request, 'login.html', context)

@login_required
def logoutView(request):
    context = {
        'title':'Orplant',
        'deskripsi':'halaman login'
    }

    if request.method == "POST":
        print(request.POST)
        if request.POST["logout"] == "Okay":
            logout(request)
        return redirect('index')
    
    
   
    print("logout")
    return render(request, 'logout.html', context)

def registerView(request):

   
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request,'register.html',context)   

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')    