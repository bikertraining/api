from django.db import models
from model_utils import FieldTracker

from utils import security


class FraudString(models.Model):
    class Type(models.TextChoices):
        ADDRESS = 'address', 'Address'
        CREDIT_CARD = 'credit_card', 'Credit Card'
        EMAIL = 'email', 'Email Address'
        IPADDRESS = 'ipaddress', 'IP Address'
        PHONE = 'phone', 'Phone Number'

    fraud_type = models.CharField(
        blank=False,
        choices=Type.choices,
        max_length=11,
        null=False
    )

    name = models.TextField(
        blank=False,
        db_index=True,
        null=False
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'fraud_string'

        default_permissions = ()

        verbose_name = 'Fraud String'
        verbose_name_plural = 'Fraud Strings'

    def __str__(self):
        return self.name

    def decrypt_credit_card(self):
        return security.decrypt_string(self.name)
