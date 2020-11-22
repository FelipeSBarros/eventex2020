from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html
        app_anem/tamplate_name"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def teste_html(self):
        """html must contin input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """html must contains CSRF"""
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_has_form(self):
        """context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name="Henrique Bastos",
                    cpf='12345678901',
                    email="henrique@bastos.net", phone='21-9911-9933')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid post should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code) #302 codigo redirect

    def test_send_subscrie_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = "contato@eventex.com.br"

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email=mail.outbox[0]
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Henrique Bastos', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('henrique@bastos.net', email.body)
        self.assertIn('21-9911-9933', email.body)

class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should noot redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_hs_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class ClassSubscribeMessage(TestCase):
    def test_message(self):
        data = dict(name="Henrique Bastos",
                    cpf='12345678901',
                    email="henrique@bastos.net", phone='21-9911-9933')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')