from django.views.generic import DetailView

from eventex.subscriptions.Mixins import EmailCreateView
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

new = EmailCreateView.as_view(
    model=Subscription,
    form_class=SubscriptionForm,
    email_subject='Confirmação de Inscrição')

detail = DetailView.as_view(model=Subscription,
                            # slug_url_kwarg="cpf_hash",
                            slug_field="cpf_hash")
