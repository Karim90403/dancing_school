from django.core.validators import RegexValidator, MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class GroupMember(models.Model):
    group = models.ForeignKey("DanceGroup", verbose_name="Группа", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client)

    class Meta:
        verbose_name = "Участник группы"
        verbose_name_plural = "Участники группы"
