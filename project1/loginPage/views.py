from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
    my_name ="Nick"
    return render(request,'home.html',{'name' : my_name})

def about(request):
    my_name ="Nick"
    return render(request,'about.html',{'name' : my_name})


def login_user(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have successfully logged in'))
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request,('Error logging in'))
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request,('Logged out'))
    return redirect('home')

