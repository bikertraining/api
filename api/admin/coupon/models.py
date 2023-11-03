from database import models


class Coupon(models.Coupon):
    class Meta:
        default_permissions = ()

        proxy = True

        verbose_name = 'Admin Coupon'
        verbose_name_plural = 'Admin Coupons'
