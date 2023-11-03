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
