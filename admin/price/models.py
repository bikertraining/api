from database import models


class Price(models.Price):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin Price'
        verbose_name_plural = 'Admin Prices'
