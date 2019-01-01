from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(label='your username',max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
