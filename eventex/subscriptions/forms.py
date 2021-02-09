from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])
    email = forms.EmailField(label="E-mail", required=False)
    phone = forms.CharField(label="Telefone", required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = name.title()
        return name

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError("informe e-mail ou Telefone.")

        return self.cleaned_data


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

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError("informe e-mail ou Telefone.")

        return self.cleaned_data

# def save(self):
    #     instance = super().save(commit=False)
    #     instance.cpf_hash = hash(instance.get('cpf'))
    #     instance.save()
    #     return instance