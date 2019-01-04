from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(label='your username',max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=8,required=True,label='输入账号')
    password1=forms.CharField(max_length=15,required=True,label='在此输入密码',widget=forms.PasswordInput)
    password2=forms.CharField(max_length=15,required=True,label='再此输入密码',widget=forms.PasswordInput)
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            print('两次密码不一致')
            raise forms.ValidationError('两次密码不一致')
        return  password2