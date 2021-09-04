import uuid

import settings.settings
from django import forms
from accounts.models import User
from accounts.tasks import send_registration_email
import django.conf

class SingUpForm(forms.ModelForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                # self.add_error('password', 'Passwords do not match.')
                raise forms.ValidationError('Passwords do not match.')

    def save(self, commit=True):
        instance = super().save(commit=commit)

        instance.username = str(uuid.uuid4())
        instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            instance.save()

        body = f'''
        Activate Your Account
        {django.conf.settings.DOMAIN}{reverse('account:activate-account', args=(instance.username,))}
        '''

        send_registration_email.delay('TODO', instance.email)

        return instance