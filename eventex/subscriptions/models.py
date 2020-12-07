from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    cpf_hash = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Inscrições'
        verbose_name = 'Inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
