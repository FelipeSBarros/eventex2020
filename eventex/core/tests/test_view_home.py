from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        # preparacao de contexto
        self.response = self.client.get(r('home'))  # client realiza requisicoes dentro do django e esta simulando acesso a urls '/'
        # usa-se o self para que ele se torne atributo da instancia e possa ser usado nos demias testes

    def test_get(self):
        """get / must return status code 200"""
        self.assertEqual(200, self.response.status_code) # expectativa, status obtido

    def test_template(self):
        """must use index.hml"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Must show kenote speakers"""
        contents = ['Grace Hopper', 'http://hbn.link/hopper-pic',
                    'Alan Turing', 'http://hbn.link/turing-pic']
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)
