from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Job, Application


def home(request):
    return render(request, 'home.html')


def jobs(request):
    all_jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': all_jobs})

def logout_user(request):
    logout(request)
    return redirect('/jobs/')



def apply_job(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES.get('resume')

        Application.objects.create(
            name=name,
            email=email,
            phone=phone,
            resume=resume
        )

        return render(request, 'success.html')

    return render(request, 'apply.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return render(request, 'success.html')

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/jobs/')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid Username or Password'
            })

    return render(request, 'login.html')