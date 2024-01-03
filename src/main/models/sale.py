from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from main.models.mixins import IdMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Sale(IdMixin):
    item = models.ForeignKey("Item", verbose_name=_("item"), on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name=_("client"), on_delete=models.CASCADE)
    count_sold = models.SmallIntegerField(_("count_sold"), validators=[MinValueValidator(0)])
    sale_date = models.DateField(_("sale_date"), auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("sale")
        verbose_name_plural = _("sales")

@receiver(pre_save, sender=Sale, dispatch_uid="create_sale")
def create_stock(sender, instance, **kwargs):
    try:
        old_instance = Sale.objects.get(id=instance.id)
        instance.item.remaining = instance.item.remaining + old_instance.count_sold
    except Sale.DoesNotExist:  # to handle initial object creation
        pass
    finally:
        if instance.item.remaining >= instance.count_sold:
            instance.item.remaining = instance.item.remaining - instance.count_sold
        else:
            instance.count_sold = instance.item.remaining
            instance.item.remaining = 0
        instance.item.save()
