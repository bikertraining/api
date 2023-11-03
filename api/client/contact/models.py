from database import models


class Contact(models.Contact):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Contact'
        verbose_name_plural = 'Client Contacts'
