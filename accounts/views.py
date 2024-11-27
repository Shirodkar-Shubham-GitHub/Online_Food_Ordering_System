from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
import os

load_dotenv()

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')

        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email, is_staff=False, is_superuser=False)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')


def token_send(request):
    return render(request , 'token_send.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        
        messages.success(request, "Your profile has been updated successfully.")
        return redirect('accounts:profile')
    
    return render(request, "edit_profile.html")



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')


def send_mail_after_registration(email , token):
    subject = 'Your account needs to be verified'
    message = f'{os.getenv("host_verify")}/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    

def verify_email(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        email_obj = User.objects.filter(email=email).first()
        if email_obj:
            send_mail_for_forgot_password(email)
            return redirect('token_send')
    return render(request, 'verify_email.html')


def forgot(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username_obj = User.objects.filter(username=username).first()
        
        try:
            if username_obj: 
                username_obj.set_password(password)
                username_obj.save()
                messages.success(request, 'Password successfully changed')
                return redirect('login_attempt')

        except Exception as e:
            print(e)

    return render(request, 'forgot.html')


def send_mail_for_forgot_password(email):
    subject = 'Change Your Account Password'
    message = f'{os.getenv("host_forgot")}/forgot/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def logout_request(request):

    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('accounts:login_attempt')
