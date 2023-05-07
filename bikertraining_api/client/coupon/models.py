from database.default import models


class Coupon(models.Coupon):
    class Meta:
        proxy = True

        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'
