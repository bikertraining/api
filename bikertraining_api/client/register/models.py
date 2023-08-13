from database.default import models


class Contact(models.Contact):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Coupon(models.Coupon):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Coupon'
        verbose_name_plural = 'Client Coupons'


class Price(models.Price):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Price'
        verbose_name_plural = 'Client Prices'


class Schedule(models.Schedule):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Schedule'
        verbose_name_plural = 'Client Schedules'
