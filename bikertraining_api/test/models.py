from database.default import models


class Schedule(models.Schedule):
    class Meta:
        proxy = True

        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
