from django.shortcuts import render, redirect 
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'User/register.html', {'form':form} )

def login(request):
    return render(request, 'User/login.html')