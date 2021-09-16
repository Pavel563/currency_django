import uuid
from django import forms
from django.conf import settings
from django.urls import reverse

from accounts.models import User
from accounts.tasks import send_registration_email


class SingUpForm(forms.ModelForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                # self.add_error('password', 'Passwords do not match.')
                raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.username = str(uuid.uuid4())
        instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            instance.save()

        body = f'''
        Activate Your Account
        {settings.DOMAIN}{reverse('account:activate-account', args=(instance.username,))}
        '''

        send_registration_email.delay(body, instance.email)

        return instance

class ChangePasswordForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('current_password', 'new_password', 'confirm_new_password')

    def clean(self):
        old_password = SingUpForm.clean(cleaned_data['password1'])
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['current_password'] !=  old_password:
                raise forms.ValidationError('Its not your old password.')
            if cleaned_data['current_password'] == cleaned_data['new_password']:
                raise forms.ValidationError('New password same as old(.')
            if cleaned_data['new_password'] != cleaned_data['confirm_new_password']:
                raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.set_password(self.cleaned_data['new_password'])

        if commit:
            instance.save()

        return instance