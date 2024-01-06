from django.core.validators import RegexValidator, MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class ClientRecord(models.Model):
    test_class = models.ForeignKey("TestClass", verbose_name="Пробное занятие", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client) + str(self.test_class)

    class Meta:
        verbose_name = "Запись клиента"
        verbose_name_plural = "Записи клиентов"
