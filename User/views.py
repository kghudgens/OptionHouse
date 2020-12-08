from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created, please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'User/register.html', {'form':form} )

def login(request):
    return render(request, 'User/login.html')