from django.db import models
from model_utils import FieldTracker


class Contact(models.Model):
    email = models.EmailField(
        blank=False,
        null=False
    )

    name = models.CharField(
        blank=False,
        max_length=255,
        null=False
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'contact'

        default_permissions = ()

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
