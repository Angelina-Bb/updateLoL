from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'email', 'body')

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

        help_texts = { "email": "Indica tu correo electrónico", "password1": "","password2": ""}

class AvatarForm(forms.Form):
    imagen = forms.ImageField()
