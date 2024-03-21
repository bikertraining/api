from database import models


class Ecourse(models.Ecourse):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin eCourse'
        verbose_name_plural = 'Admin eCourse'
