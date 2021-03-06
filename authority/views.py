from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from authority.forms import *
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

def signup_admin(request):
    template_name="signup_admin.html"
    data = {}
    #if request.method == 'POST':
    form_admin = SignUpAdminForm(request.POST or None)

    if form_admin.is_valid():
        form_admin.save()
        password = form_admin.cleaned_data.get('password1')
        username = form_admin.cleaned_data.get('username')
        print(type(username))
        user = authenticate(username=username, password=password)
        messages.success(request, 'Cuenta creada con éxito')
        login(request, user)
        return redirect("home")
    data['form'] = form_admin
    return render(request,template_name,data)
@login_required(login_url="/")
def logout_admin(request):
    logout(request)
    return redirect("home")
def login_admin(request):
    template_name = "login.html"
    data = {}
    logout(request)
    username = password = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                messages.warning(request,"Usuario o contraseña incorrecta")
        else:
            #usuario no existe
            messages.error(request,"Usuario o contraseña incorrecta")
    return render(request,template_name)
