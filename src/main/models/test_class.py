from django.db import models
from main.models.mixins import IdMixin


class TestClass(IdMixin):
    choreographer = models.ForeignKey("Сhoreographer", verbose_name="Хореограф", on_delete=models.CASCADE)
    class_date = models.DateField("Дата занятия")
    class_time = models.TimeField("Время занятия")

    def __str__(self):
        return str(self.choreographer) + ":" + str(self.class_date) + " " + str(self.class_time)

    class Meta:
        verbose_name = "Пробное занятие"
        verbose_name_plural = "Пробные занятия"
        unique_together = (
            "choreographer",
            "class_date",
            "class_time",
        )
