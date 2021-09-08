from django import forms

from currency.models import Rate, Bank, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type',
            'sale',
            'buy',
            'bank',
        )


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = (
            'name',
            'url',
            'logo',
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )
