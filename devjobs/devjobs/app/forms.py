from django import forms
from django.contrib.auth.models import User
from app.models import jobInfo

class userInfoForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'box','placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'box', 'placeholder': 'Email id'}),
            'password': forms.PasswordInput(attrs={'class': 'box', 'placeholder': 'Password'}),
        }
        help_texts = {
            'username': None,
        }
        labels = {
       'username' : '',
       'email' : '',
       'password' : '',
       }


class jobInfoForm(forms.ModelForm):

    class Meta():
        model = jobInfo
        fields = "__all__"
        widgets = {
            'jobRole': forms.TextInput(attrs={'class': 'box','placeholder': 'Job Title'}),
            'jobDescription': forms.TextInput(attrs={'class': 'box','placeholder': 'Description'}),
            'jobLocation': forms.TextInput(attrs={'class': 'box','placeholder': 'Location'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'box','placeholder': 'Phone Number'}),
        }
        labels = {
       'jobRole' : '',
       'jobDescription' : '',
       'jobLocation' : '',
       'phoneNumber' : '',
       }
