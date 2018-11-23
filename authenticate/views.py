from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def subscribe_plan(request):
 if request.user.is_authenticated:
    if request.method == 'POST':
        sub_form = ProfileForm(request.POST, instance=request.user.profile)
        if sub_form.is_valid():
            sub_form.save()
            messages.success(request, ('Your subscription plan was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))

    else:
        sub_form = ProfileForm(instance=request.user.profile)
        context = {'sub_form': sub_form}
        return render(request, 'authenticate/subscribe.html', context)
 else:
    return redirect('login')



def home(request):
    return render(request, 'authenticate/home.html', {})

def pricing(request):
    return render(request, 'authenticate/pricing.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In!'))
            return redirect('home')

        else:
            messages.success(request, ('Error Logging In - Please Try Again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect ('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Successfully Registered!'))
            return redirect('pricing')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        sub_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and sub_form.is_valid():
            form.save()
            sub_form.save()
            messages.success(request, ('Your Profile Changes Have Been Saved'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        sub_form = ProfileForm(instance=request.user.profile)
    context = {'form': form, 'sub_form': sub_form}
    return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You Have Changed Your Password'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)
