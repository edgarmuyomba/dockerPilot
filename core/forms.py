from django import forms 
from .models import User

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'