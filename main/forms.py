from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class AddTodoForm(forms.Form):
    content = forms.CharField()
