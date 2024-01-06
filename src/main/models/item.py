from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusChoice(models.TextChoices):
    YES = "Yes", "Да"
    NO = "No", "Нет"


class Item(IdMixin):
    AVAILABILITY_CHOICES = (("YES", "Да"), ("NO", "Нет"))
    name = models.CharField(verbose_name="Название товара", max_length=30)
    price = models.IntegerField(verbose_name="Цена", validators=[MinValueValidator(0)])
    remaining = models.SmallIntegerField("Осталось", validators=[MinValueValidator(0)])
    availability = models.CharField(verbose_name="Наличие", max_length=3, choices=StatusChoice.choices)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


@receiver(pre_save, sender=Item, dispatch_uid="create_sale")
def create_stock(sender, instance, **kwargs):
    if instance.remaining > 0:
        instance.availability = StatusChoice.YES
    else:
        instance.availability = StatusChoice.NO
