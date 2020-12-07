from django.forms import forms 
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.Form):
    
    class Meta:
        fields =['username', 'email', 'password1', 'password2']
    