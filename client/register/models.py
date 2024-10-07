from database import models


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


class Register(models.Register):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Register'
        verbose_name_plural = 'Client Registrations'


class Schedule(models.Schedule):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Client Schedule'
        verbose_name_plural = 'Client Schedules'
