from database.default import models


class Coach(models.Coach):
    class Meta:
        ordering = [
            'name'
        ]

        proxy = True

        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'
