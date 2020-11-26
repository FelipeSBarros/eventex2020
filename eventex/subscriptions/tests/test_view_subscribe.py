from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):
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
        """html must contain input tags"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


    def test_csrf(self):
        """html must contains CSRF"""
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_has_form(self):
        """context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostValid(TestCase):
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

class SubscribePostInvalid(TestCase):
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

class ClassSubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name="Henrique Bastos",
                    cpf='12345678901',
                    email="henrique@bastos.net", phone='21-9911-9933')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')