from django.db import models

from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, validators=[validate_cpf])
    email = models.EmailField('E-mail', blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cpf_hash = models.CharField(max_length=20)
    paid = models.BooleanField("Pago", default=False)

    class Meta:
        verbose_name_plural = 'Inscrições'
        verbose_name = 'Inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subscriptions:detail', self.cpf_hash)