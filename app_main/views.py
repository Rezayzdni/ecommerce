from django.http import HttpResponse
from django.shortcuts import render,redirect
from app_main.models import Product
from django.contrib import messages
# from .forms import UserRegisterForm , UserUpdateForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from app_user import forms
from django.contrib.auth.models import User


def home(request):
    ctx = {}
    ctx['products'] = Product.objects.all()
    return render(request, 'app_main/first-page.html' , ctx)


def music_detail(request):
    return render(request, 'app_main/music-detail.html')


def music_detail_detail(request):
    return render(request, 'app_main/music-detail-detail.html')


# def customer_profile(request):
#     return render(request, 'app_main/customer-profile.html')



@login_required
def customer_profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST , instance=request.user)
        print("let se what are the request.FILES" , request.FILES)
        p_form = forms.ProfileUpdateForm(request.POST ,request.FILES , instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'your account has been updated !')
            return redirect('profile',name=request.user.username)          
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form' : u_form,
        'p_form' : p_form
    }
    
    
    return render(request , 'app_main/customer-profile.html',context )























def solve_exercise(request):
    return render(request, 'app_main/solve-exercise.html')


def my_saved_products(request):
    return render(request, 'app_main/my-saved-products.html')


def custom_profile_detail(request):
    return render(request, 'app_main/customer-profile-detail.html')


def custom_profile_settings(request):
    return render(request, 'app_main/customer-profile-settings.html')


def contact_us(request):
    return HttpResponse('contact us')
