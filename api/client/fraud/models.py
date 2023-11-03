from database import models


class FraudString(models.FraudString):
    class Meta:
        default_permissions = ()

        ordering = [
            'name'
        ]

        proxy = True

        verbose_name = 'Client Fraud String'
        verbose_name_plural = 'Client Fraud Strings'
