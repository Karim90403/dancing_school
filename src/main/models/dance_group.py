from django.db import models
from main.models.mixins import IdMixin


class DanceGroup(IdMixin):
    choreographer = models.ForeignKey("Сhoreographer", verbose_name="Хореограф", on_delete=models.CASCADE)
    dance_style = models.CharField("Стиль танцев", max_length=30)

    def __str__(self):
        return str(self.choreographer) + " Стиль: " + str(self.dance_style)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
