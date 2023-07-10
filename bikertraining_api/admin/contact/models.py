from database.default import models


class Contact(models.Contact):
    class Meta:
        proxy = True

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
