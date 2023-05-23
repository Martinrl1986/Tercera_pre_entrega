from django import forms
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import PortfolioItem, ContactMessage, SocialLink, SearchForm
from blogapp.models import CustomUser
from blogapp.models import About

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['image', 'caption', 'target_modal']
        
        
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['name', 'url']

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ('image', 'caption', 'target_modal')

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'message')

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
    
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'description']
        
class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=150)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'password1', 'password2')