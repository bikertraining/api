from django.db import models
from model_utils import FieldTracker


class Ecourse(models.Model):
    link = models.URLField(
        blank=False,
        null=False
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'ecourse'

        default_permissions = ()

        verbose_name = 'eCourse'
        verbose_name_plural = 'eCourse'

    def __str__(self):
        return self.link
