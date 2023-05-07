from database.default import models


class Contact(models.Contact):
    class Meta:
        proxy = True

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Coupon(models.Coupon):
    class Meta:
        proxy = True

        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'


class Price(models.Price):
    class Meta:
        proxy = True

        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


class Schedule(models.Schedule):
    class Meta:
        proxy = True

        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
