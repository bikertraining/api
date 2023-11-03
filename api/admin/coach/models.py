from database import models


class Coach(models.Coach):
    class Meta:
        default_permissions = ()

        ordering = [
            'name'
        ]

        proxy = True

        verbose_name = 'Admin Coach'
        verbose_name_plural = 'Admin Coaches'
