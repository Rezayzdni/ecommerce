from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.forms import DateInput
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phoneNumber = forms.CharField(max_length = 16)
    username = forms.CharField(max_length = 64)
    class Meta:
        model = User
        fields = ['username', 'email' , 'phoneNumber']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [ 'phoneNumber' ]
       

# from .models import Profile
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image', 'phoneNumber', 'currentLocation']
#         widgets = {
#             'image': forms.FileInput(),
#         }
#         labels = {
#             'image': 'Profile Photo',
#         }


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User 
#         fields = ['username' , 'email' , 'password1' , 'password2']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User 
#         fields = ['username' , 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']



