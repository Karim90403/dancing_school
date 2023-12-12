from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class TestClass(IdMixin):
    choreographer = models.ForeignKey("Сhoreographer", verbose_name=_("choreographer"), on_delete=models.CASCADE)
    class_date = models.DateField(_("class_date"))
    class_time = models.TimeField(_("class_time"))

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("test_class")
        verbose_name_plural = _("test_classes")
