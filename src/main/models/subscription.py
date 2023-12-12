import datetime

from django.core.validators import MinValueValidator
from pydantic import ValidationError

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscription(IdMixin):
    STATUS_CHOICES = (("ACTIVE", _("Active")), ("SUSPENDED", _("Suspended")))
    client = models.ForeignKey("Client", verbose_name=_("client"), on_delete=models.CASCADE)
    lessons_left = models.SmallIntegerField(_("lessons_left"), validators=[MinValueValidator(1)], null=True)
    summ_lessons = models.SmallIntegerField(_("summ_lessons"), validators=[MinValueValidator(1)], default=10)
    start_date = models.DateField(_("start_date"))
    end_date = models.DateField(_("end_date"))
    status = models.CharField(_("subscription_status"),  max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError("The start date cannot be bigger then end date!")
        if self.lessons_left > self.summ_lessons:
            raise ValidationError("The sum of lessons left cannot be bigger then summ of lessons date!")
        super(Subscription, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")
