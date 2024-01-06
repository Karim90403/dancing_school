from django.core.validators import RegexValidator, MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(IdMixin):
    GENDER_CHOICES = (("M", "М"), ("F", "Ж"))
    fio = models.CharField("Фио", max_length=90)
    birthday = models.DateField("Дата рождения")
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES)
    phone = models.BigIntegerField("Номер телефона", validators=[MinValueValidator(111111)], unique=True)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
