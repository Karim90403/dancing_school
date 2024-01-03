from django.core.validators import RegexValidator, MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class GroupMember(models.Model):
    group = models.ForeignKey("DanceGroup", verbose_name=_("group"), on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name=_("client"), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client) + str(self.group)

    class Meta:
        verbose_name = _("group_member")
        verbose_name_plural = _("group_members")
