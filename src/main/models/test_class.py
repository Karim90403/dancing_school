from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class TestClass(IdMixin):
    choreographer = models.ForeignKey("Сhoreographer", verbose_name="Хореограф", on_delete=models.CASCADE)
    class_date = models.DateField("Дата занятия")
    class_time = models.TimeField("Время занятия")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Пробное занятие"
        verbose_name_plural = "Пробные занятия"
