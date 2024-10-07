from django.db import models


class Register(models.Model):
    schedule = models.ForeignKey(
        'Schedule',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='register_schedule',
        verbose_name='Schedule'
    )

    address = models.TextField(
        blank=False,
        null=True
    )

    amount = models.TextField(
        blank=False,
        null=True
    )

    city = models.TextField(
        blank=False,
        null=True
    )

    class_type = models.TextField(
        blank=False,
        null=True
    )

    comment = models.TextField(
        blank=True,
        null=True
    )

    coupon_code = models.TextField(
        blank=True,
        null=True
    )

    credit_card_number = models.TextField(
        blank=False,
        null=True
    )

    dln = models.TextField(
        blank=False,
        null=True
    )

    dls = models.TextField(
        blank=False,
        null=True
    )

    dob = models.TextField(
        blank=False,
        null=True
    )

    email = models.TextField(
        blank=False,
        null=True
    )

    first_name = models.TextField(
        blank=False,
        null=True
    )

    last_name = models.TextField(
        blank=False,
        null=True
    )

    phone = models.TextField(
        blank=False,
        null=True
    )

    schedule_date = models.TextField(
        blank=False,
        null=True
    )

    schedule_day = models.TextField(
        blank=False,
        null=True
    )

    state = models.TextField(
        blank=False,
        null=True
    )

    xpl = models.TextField(
        blank=False,
        null=True
    )

    zipcode = models.TextField(
        blank=False,
        null=True
    )

    class Meta:
        db_table = 'register'

        default_permissions = ()

        verbose_name = 'Register'
        verbose_name_plural = 'Registration'

    def __str__(self):
        return self.schedule
