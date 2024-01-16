from django.db import models
from main.models.mixins import IdMixin


class Schedule(IdMixin):
    group = models.ForeignKey("DanceGroup", verbose_name="Группа", on_delete=models.CASCADE)
    class_date = models.DateField("Дата занятия")
    class_time = models.TimeField("Время занятия")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
