from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class DanceGroup(IdMixin):
    members = models.ManyToManyField("Client", verbose_name=_("members"), related_name="group", blank=True)
    choreographer = models.ForeignKey("Сhoreographer", verbose_name=_("choreographer"), on_delete=models.CASCADE)
    dance_style = models.CharField(_("dance_style"), max_length=30)

    def __str__(self):
        return str(self.id) + str(self.choreographer) + str(self.dance_style)

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
