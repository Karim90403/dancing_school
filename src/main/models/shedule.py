from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Schedule(IdMixin):
    group = models.ForeignKey("DanceGroup", verbose_name=_("group"), on_delete=models.CASCADE)
    class_date = models.DateField(_("class_date"))
    class_time = models.TimeField(_("class_time"))

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")
