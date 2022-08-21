from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateUserForm, ChangePassword, ForgotPassword,SetNewPassword


# Create your views here.


def check_auth(request):
    if not request.user.is_authenticated:
        return log_in(request)

def account(request): #About page
    check_auth(request)

    return render(request,'main/account.html',locals())


def index(request): #Home page
    return render(request,'main/index.html')

def registration(request): #sign in page
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            print(request, "Registration successful.")
            logout(request)

            return redirect('/login', foo='bar') #Page after registration!

        else:
            print(request, "Unsuccessful registration. Invalid information.")
            mes="Unsuccessful registration. Invalid information."
            render(request, 'main/registration.html', locals())

    form = CreateUserForm
    return render(request,'main/registration.html', locals())

    # return render(request,'main/registration.html',locals())

def about(request): #About page
    return HttpResponse("<h4>About page</h4>")


def contact_us(request): #contact page
    return HttpResponse("<h4>contact page</h4>")

def log_in(request):
    print(request.method)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print('Authenticated successfully')
                    return account(request)
                else:
                    print('Disabled account')
                    error = 'Disabled account'
                    render(request, 'main/login.html', locals())
            else:
                print('Invalid login')
                error='*wrong login or password :('
                return render(request, 'main/login.html', locals())
    else:
        form = LoginForm()
    return render(request, 'main/login.html', locals())



def change_passport(request):

    check_auth(request)

    form = ChangePassword(request.user)

    if request.method == "POST":
        form = ChangePassword(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login', foo='bar')


        else:
            mes="Wrong passwords"

    return render(request, 'main/change_password.html',locals())


def forgot_password(request):
    form = ForgotPassword(request.POST)

    if request.method == "POST":
        form = ForgotPassword(request.POST)
        if form.is_valid():
            form.save()
            mes='Email sent. Check Your email box'
            return render(request, 'main/forgot_password.html',locals())

        else:
            mes = "Wrong email"

    return render(request, 'main/forgot_password.html',locals())



def set_new_password(request):
    form = SetNewPassword(request.POST)

    if request.method == "POST":
        form = SetNewPassword(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login', foo='bar')

        else:
            mes = "Wrong passwords"

    return render(request, 'main/set_new_password.html',locals())