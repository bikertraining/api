from database.default import models


class Ecourse(models.Ecourse):
    class Meta:
        proxy = True

        verbose_name = 'Ecourse'
        verbose_name_plural = 'Ecourse'
