from django.core.validators import MinValueValidator
from django.db import models
from main.models.mixins import IdMixin


class Сhoreographer(IdMixin):
    GENDER_CHOICES = (("M", "М"), ("F", "Ж"))
    fio = models.CharField("ФИО", max_length=90)
    birthday = models.DateField("Дата рождения")
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES)
    phone = models.BigIntegerField("Номер телефона", validators=[MinValueValidator(111111)], unique=True)
    stage = models.SmallIntegerField("Стаж", validators=[MinValueValidator(1)])
    dance_style = models.CharField("Стиль танцев", max_length=30)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = "Хореограф"
        verbose_name_plural = "Хореографы"
