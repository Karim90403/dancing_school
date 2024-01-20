from django.db import models
from main.models.dance_group import DanceGroup
from main.models.mixins import IdMixin


class Schedule(IdMixin):
    group = models.ForeignKey("DanceGroup", verbose_name="Группа", on_delete=models.CASCADE)
    class_date = models.DateField("Дата занятия")
    class_time = models.TimeField("Время занятия")

    def save(self, *args, **kwargs):
        schedules = Schedule.objects.all().filter(class_date=self.class_date, class_time=self.class_time)
        groups = DanceGroup.objects.all().filter(choreographer=self.group.choreographer)
        for schedule in schedules:
            for group in groups:
                if schedule != self and group != self.group:
                    if schedule.group == group:
                        return 0
        super(Schedule, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        unique_together = (
            "group",
            "class_date",
            "class_time",
        )
