from database.default import models


class Price(models.Price):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Price'
        verbose_name_plural = 'Client Prices'
