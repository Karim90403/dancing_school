import datetime

from django.core.validators import MinValueValidator
from pydantic import ValidationError

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscription(IdMixin):
    STATUS_CHOICES = (("ACTIVE", "Активен"), ("SUSPENDED", "Закончен"))
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)
    lessons_left = models.SmallIntegerField("Прошло занятий", validators=[MinValueValidator(1)], null=True)
    summ_lessons = models.SmallIntegerField("Всего зантий", validators=[MinValueValidator(1)], default=10)
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата конца")
    status = models.CharField("Статус абоенемента",  max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError("The start date cannot be bigger then end date!")
        if self.lessons_left > self.summ_lessons:
            raise ValidationError("The sum of lessons left cannot be bigger then summ of lessons date!")
        super(Subscription, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
