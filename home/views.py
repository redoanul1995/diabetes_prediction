from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'home/signup.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('predict')
        else:
            messages.warning(request, 'invalid credentials')
    return render(request, 'home/home.html', {})
