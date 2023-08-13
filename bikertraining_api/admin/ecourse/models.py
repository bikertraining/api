from database.default import models


class Ecourse(models.Ecourse):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin Ecourse'
        verbose_name_plural = 'Admin Ecourse'
