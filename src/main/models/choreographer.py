# choreographer
from django.core.validators import MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Сhoreographer(IdMixin):
    GENDER_CHOICES = (("M", _("M")), ("F", _("F")))
    fio = models.CharField(_("fio"), max_length=90)
    birthday = models.DateField(_("birthday"))
    gender = models.CharField(_("gender"), max_length=1, choices=GENDER_CHOICES)
    phone = models.BigIntegerField(_("phone"), validators=[MinValueValidator(111111)], unique=True)
    stage = models.SmallIntegerField(_("stage"), validators=[MinValueValidator(1)])
    dance_style = models.CharField(_("dance_style"), max_length=30)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = _("choreographer")
        verbose_name_plural = _("choreographers")
