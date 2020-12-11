from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        ur_form = UserRegisterForm(request.POST)
        # import pdb; pdb.set_trace()

        if ur_form.is_valid():
            #username = ur_form.cleaned_data.get('username')
            ur_form.save()
            # request.user.profile.phone_number = ur_form.cleaned_data.get('phonenumber')
            messages.success(request, 'حساب شما با موفقیت ایجاد شد!')
            user = authenticate(username=ur_form.cleaned_data['username'], password=ur_form.cleaned_data['password1'])
            if user is not None:
                login(request,user)

                ur_up_form = UserUpdateForm(request.POST , instance=user.profile)
                ur_up_form.save()
                print("phonenumber is " , user.profile.phoneNumber)
            return redirect('home')

    else:
        ur_form = UserRegisterForm()
    context = {
        'ur_form': ur_form,
    }
    return render(request, 'app_user/register.html', context)





#***************************************************************************************userprofile

# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from app_user.forms import UserUpdateForm
# from app_userprofile.forms import UserProfileForm
#
#
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         uu_form = UserUpdateForm(request.POST, instance=request.app_user)
#         pu_form = UserProfileForm(request.POST, request.FILES, instance=request.app_user.profile)
#         if uu_form.is_valid() and pu_form.is_valid():
#             uu_form.save()
#             pu_form.save()
#             messages.success(request, f'Your account has been updated successfully!')
#             return redirect('app_user-profile')
#     else:
#         uu_form = UserUpdateForm(instance=request.app_user)
#         pu_form = UserProfileForm(instance=request.app_user.profile)
#     context = {
#         'uu_form': uu_form,
#         'pu_form': pu_form,
#     }
#     return render(request, 'users/profile.html', context)

