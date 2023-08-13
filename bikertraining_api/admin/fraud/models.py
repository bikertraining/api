from database.default import models


class FraudString(models.FraudString):
    class Meta:
        default_permissions = ()

        ordering = [
            'name'
        ]

        proxy = True

        verbose_name = 'Admin Fraud String'
        verbose_name_plural = 'Admin Fraud Strings'
