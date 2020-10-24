from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"input100",
                "type":"text",
                "name":"username",
                "placeholder":"Username"
            }
        )
    ) 
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"input100",
                "type":"text",
                "name":"email",
                "placeholder":"Email"
            }
        )
    )
    password1= forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs = {
                "class":"input100",
                "type":"password",
                "name":"pass",
                "placeholder":"Password",
            }
        )
    )
    password2= forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs = {
                 "class":"input100",
                "type":"password",
                "name":"pass",
                "placeholder":"Confirm Password",
            }
        )
    )
    def clean(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        email = self.cleaned_data.get("email")
        qs1 = User.objects.filter(email__iexact=email)
      
        if qs.exists():
            self.add_error("username", 'This is invalid username, please pick another')

        elif password1 != password2:
            self.add_error('password1','Password does not match')

        elif qs1.exists():
            self.add_error("email", 'Email already in use')


    # def clean_password1(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 != password2:
    #         raise forms.ValidationError('Password Does not match',code='invalid')

    

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = User.objects.filter(username__iexact=username)
    #     if qs.exists():
    #         raise forms.ValidationError("This is an invalid username, please pick another.", code='invalid')
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     qs = User.objects.filter(email__iexact=email)
    #     if qs.exists():
    #         raise forms.ValidationError("Email already in use.", code='invalid')
    #     return email


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "class":"input100",
                "type":"text",
                "name":"username",
                "placeholder":"Username"
            }
        )
    ) 
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                "class":"input100",
                "type":"password",
                "name":"pass",
                "placeholder":"Password",
            }
        )
    )

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user ")
        return username