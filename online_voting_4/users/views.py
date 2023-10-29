from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from datetime import datetime
from django.contrib import messages
from users.forms import SignUpForm, LogInForm, UserProfileForm


def home(request):
    now = datetime.now()
    current_year = now.year
    
    return render(request, 'home.html', {
        "current_year": current_year,
    })


def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            form.save()
            logout(request)
            messages.success(request, ("Registration successfull!!"))
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {
        'form': form,
    })


# 1st way for login
def log_in(request):
    form = LogInForm
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            form = LogInForm()

    return render(request, 'authenticate/login.html', {'form': form})


# 2nd way for login
# def log_in(request):

#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, ("Logged in successfully!!!!"))
#             return redirect('home')
#         else:
#             messages.success(request, ("There was an error logging in!!! Try again..."))
#             return redirect('login')
#     else:
#         return render(request, 'authenticate/login.html', {})


def log_out(request):
    logout(request)
    messages.success(request, ("Logged out successfully!!!"))
    return redirect('home')


def user_profile(request, user_id):
    User = get_user_model()
    user_info = User.objects.get(pk=user_id)
    return render(request, 'authenticate/profile.html', {
        'user_info': user_info,
    })

def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Successfully updated profile!!!"))
            return redirect('home')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'authenticate/update_profile.html', {
        'form': form,
    })

def about_us(request):
    return render(request, 'about_us.html')