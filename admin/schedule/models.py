from database import models


class Price(models.Price):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin Price'
        verbose_name_plural = 'Admin Prices'


class Schedule(models.Schedule):
    class Meta:
        default_permissions = ()

        ordering = [
            'date_from'
        ]

        proxy = True

        verbose_name = 'Admin Schedule'
        verbose_name_plural = 'Admin Schedules'
