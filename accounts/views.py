from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm

User = get_user_model()
def register_view(request):
    if not request.user.is_anonymous:
        return redirect("/") 
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1
    return render(request, "accounts/form.html", {"form": form, 'register':True})



def login_view(request):
    if not request.user.is_anonymous:
        return redirect("/") 
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            #user is valid and active -> is_active
            #request.user == user
            login(request, user)
            return redirect('/')
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect('/invalid-password')
            request.session['invalid_user'] = 1 # 1 == True
        
    return render(request, "accounts/form.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/login')