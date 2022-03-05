from database.default import models


class Schedule(models.Schedule):
    class Meta:
        ordering = [
            'date_from'
        ]

        proxy = True

        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
