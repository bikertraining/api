from django.db import models
from model_utils import FieldTracker


class Price(models.Model):
    class ClassType(models.TextChoices):
        BRC = 'brc', 'Basic RiderCourse'
        ERC = 'erc', 'Experienced RiderCourse'
        IME = 'ime', 'Kickstart'
        PRIVATE = 'private', 'Private'
        THREEWBRC = '3wbrc', 'Three-Wheeled Basic RiderCourse'

    amount = models.DecimalField(
        blank=False,
        decimal_places=2,
        default=0.00,
        max_digits=10,
        null=False
    )

    class_type = models.CharField(
        blank=False,
        choices=ClassType.choices,
        max_length=7,
        null=False
    )

    is_active = models.BooleanField(
        default=True
    )

    process_amount = models.DecimalField(
        blank=False,
        decimal_places=2,
        default=0.00,
        max_digits=10,
        null=False
    )

    re_amount = models.DecimalField(
        blank=False,
        decimal_places=2,
        default=0.00,
        max_digits=10,
        null=False
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'price'

        default_permissions = ()

        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        return self.get_class_type_display()
