from django.db import models


class Coach(models.Model):
    address = models.CharField(
        blank=False,
        max_length=255,
        null=False
    )

    city = models.CharField(
        blank=False,
        max_length=255,
        null=False
    )

    date_to = models.DateField(
        auto_now_add=False
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    frtp_date_from = models.DateField(
        auto_now_add=False
    )

    is_active = models.BooleanField(
        default=True
    )

    msf_id = models.CharField(
        blank=True,
        max_length=20,
        null=True
    )

    name = models.CharField(
        blank=False,
        max_length=255,
        null=False
    )

    phone = models.CharField(
        blank=False,
        max_length=255,
        null=False
    )

    state = models.CharField(
        blank=False,
        max_length=3,
        null=False
    )

    zipcode = models.CharField(
        blank=False,
        max_length=16,
        null=False
    )

    class Meta:
        db_table = 'coach'

        default_permissions = ()

        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'

    def __str__(self):
        return self.name
