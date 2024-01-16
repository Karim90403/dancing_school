from django.db import models
from django.utils.translation import gettext_lazy as _


class IdMixin(models.Model):
    id = models.AutoField(_("id"), primary_key=True)

    class Meta:
        abstract = True
