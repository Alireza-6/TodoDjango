from django.contrib.auth.forms import UserChangeForm
from django import forms

from users.models import CustomUser


class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter You Email Address'}),
        label='Email',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label='Confirm Password'
    )

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('re_password')
        if confirm_password != password:
            raise forms.ValidationError('passwords do not match')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist_user_email = CustomUser.objects.filter(email=email).exists()
        if is_exist_user_email:
            raise forms.ValidationError('this email already exists')
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name')
