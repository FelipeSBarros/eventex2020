from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
             name="Felipe",
             cpf='12345678901',
             email='felipe.b4rros@gmail.com',
             phone='21-9911-9933')
        self.obj.cpf_hash = hash(self.obj.cpf)
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_has_hash(self):
        """Subscription must have an auto created hash based on cpf field"""
        self.assertIsInstance(self.obj.cpf_hash, int)

    def test_cpfhash(self):
        """cpfHash field must be equal to hash(cpf)"""
        self.assertEqual(self.obj.cpf_hash, hash(self.obj.cpf))

    def test_str(self):
        self.assertEqual('Felipe', str(self.obj))
