import datetime

from django.core.validators import MinValueValidator
from django.db import models
from main.models.mixins import IdMixin


class Subscription(IdMixin):
    STATUS_CHOICES = (("ACTIVE", "Активен"), ("SUSPENDED", "Закончен"))
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)
    lessons_left = models.SmallIntegerField("Прошло занятий", validators=[MinValueValidator(1)], null=True)
    summ_lessons = models.SmallIntegerField("Всего зантий", validators=[MinValueValidator(1)], default=10)
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата конца")
    status = models.CharField("Статус абоенемента", max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    def __str__(self):
        return str(self.client) + ": " + str(self.start_date) + "-" + str(self.end_date)

    def save(self, *args, **kwargs):
        for el in Subscription.objects.all().filter(client=self.client):
            if el.status == "ACTIVE" and el.end_date > self.start_date and el != self:
                return "exist active"
            elif ((el.end_date > self.start_date > el.start_date) or (
                    el.start_date < self.end_date < el.end_date)) and el != self:
                return "time"
        if self.start_date > self.end_date:
            return "time"
        elif self.lessons_left > self.summ_lessons:
            return "number"
        if self.end_date < datetime.date.today() or self.lessons_left == self.summ_lessons:
            self.status = "SUSPENDED"
        else:
            self.status = "ACTIVE"
        super(Subscription, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
