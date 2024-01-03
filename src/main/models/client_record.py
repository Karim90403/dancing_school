from django.core.validators import RegexValidator, MinValueValidator

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class ClientRecord(models.Model):
    test_class = models.ForeignKey("TestClass", verbose_name=_("test_class"), on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name=_("client"), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client) + str(self.test_class)

    class Meta:
        verbose_name = _("client_record")
        verbose_name_plural = _("client_records")
