from django.core.validators import MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(IdMixin):
    AVAILABILITY_CHOICES = (("YES", _("Yes")), ("NO", _("No")))
    name = models.CharField(_("item_name"), max_length=30)
    price = models.IntegerField(_("price"), validators=[MinValueValidator(0)])
    remaining = models.SmallIntegerField(_("remaining"), validators=[MinValueValidator(1)])
    availability = models.CharField(_("availability"), max_length=3, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
