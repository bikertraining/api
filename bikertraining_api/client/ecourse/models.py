from database.default import models


class Ecourse(models.Ecourse):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Ecourse'
        verbose_name_plural = 'Client Ecourse'
