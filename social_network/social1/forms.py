from dataclasses import fields
from django import forms
from django.contrib.auth.models import User

class LoginUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['username'].help_text = None

    # username = forms.CharField(max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = 'username', 'password'
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) > 20:
            raise forms.ValidationError('Length of password is more than allowed 20 symbols')
        return password
