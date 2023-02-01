from django.db import models
from model_utils import FieldTracker


class Ecourse(models.Model):
    link_brc = models.URLField(
        blank=False,
        null=False
    )

    link_3wbrc = models.URLField(
        blank=False,
        null=False
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'ecourse'

        default_permissions = ()

        verbose_name = 'eCourse'
        verbose_name_plural = 'eCourse'
