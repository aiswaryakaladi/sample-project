from django import forms
from .models import *
from django.contrib.auth.models import User


class regform(forms.Form):
    cname=forms.CharField(max_length=25)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)
    phone = forms.IntegerField()
    address=forms.CharField(max_length=25)

class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class pageform(forms.Form):
    cname = forms.CharField(max_length=30)
    email = forms.EmailField()
    jname = forms.CharField(max_length=30)
    jtype = forms.CharField(max_length=30)
    wtype = forms.CharField(max_length=30)
    exp = forms.CharField(max_length=30)

class userreg(forms.ModelForm):
    class Meta:
        model= User
        fields= '__all__'

class userlog(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class profileform(forms.Form):
    image = forms.FileField()
    fname = forms.CharField(max_length=20)
    email = forms.EmailField()
    resume = forms.FileField()
    education = forms.CharField(max_length=20)
    exp = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)
    phone = forms.IntegerField()

class applyform(forms.Form):
    company = forms.CharField(max_length=40)
    title = forms.CharField(max_length=40)
    fname = forms.CharField(max_length=40)
    email = forms.EmailField()
    resume = forms.FileField()
    education = forms.CharField(max_length=20)
    exp = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)
    phone = forms.IntegerField()












