from django import forms
from django.core.exceptions import ValidationError

from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        name = name.title()
        return name

    def clean(self):
        self.cleaned_data = super().clean()
        self.cleaned_data['cpf_hash'] = hash(self.cleaned_data.get('cpf'))

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError("informe e-mail ou Telefone.")

        return self.cleaned_data
