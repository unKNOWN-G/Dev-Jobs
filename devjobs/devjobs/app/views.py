from django.shortcuts import render
from app.forms import userInfoForm,  jobInfoForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'app/index.html')

## For Login and Authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_register(request):
    registered = False

    if request.method == "POST":
        user_form = userInfoForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = userInfoForm()

    return render(request,'app/userreg.html',context = {'user_form' : user_form,'registered' : registered})

@login_required
def job_register(request):
    registered = False

    if request.method == "POST":
        user_form = jobInfoForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = jobInfoForm()

    return render(request,'app/jobreg.html',context = {'user_form' : user_form,'registered' : registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def special(request):
    return render(request, 'app/dashboard.html', {})

def invalid(request):
    return render(request, 'app/invalid.html', {})

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            messages.error(request,'username or password not correct')
            return HttpResponseRedirect(reverse('login'))

    else:
        return render(request, 'app/login.html', {})
