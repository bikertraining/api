from database.default import models


class Contact(models.Contact):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin Contact'
        verbose_name_plural = 'Admin Contacts'
