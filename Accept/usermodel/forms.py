from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'full_name']

    def clean_email(self):
        email = self.changed_data['email']
        user = User.objects.filter(email=email).exists()

        if user:
            raise ValidationError('This is email already exists.')
        return email


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="for your password change click <a href=\"../password/\">this here</a>")

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'is_active', 'is_admin']
