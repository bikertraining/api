from database import models


class Register(models.Register):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin Register'
        verbose_name_plural = 'Admin Registration'
